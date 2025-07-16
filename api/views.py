from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import Paragraph, WordMapping
from django.db import transaction
from django.db.models import Count
import re


class ParagraphUploadView(APIView):
    """
    Upload multiple paragraphs separated by two line breaks (\n\n)
    Each paragraph will be saved, and words inside will be tokenized and indexed.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        text = request.data.get("text", "")
        if not text:
            return Response({"error": "Text is required."}, status=status.HTTP_400_BAD_REQUEST)

        # Split text into paragraphs based on double line breaks
        paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
        if not paragraphs:
            return Response({"error": "No valid paragraphs found."}, status=status.HTTP_400_BAD_REQUEST)

        created_paragraphs = []

        with transaction.atomic():
            for para in paragraphs:
                # Save paragraph
                paragraph = Paragraph.objects.create(text=para)
                created_paragraphs.append(paragraph)

                # Tokenize words (remove punctuations, lowercase)
                words = re.findall(r'\b\w+\b', para.lower())
                word_objects = [
                    WordMapping(word=word, paragraph=paragraph) for word in words
                ]
                WordMapping.objects.bulk_create(word_objects)

        return Response({
            "message": "Paragraphs uploaded and indexed successfully.",
            "paragraphs_created": len(created_paragraphs)
        }, status=status.HTTP_201_CREATED)


class WordSearchView(APIView):
    """
    Search for a word and return top 10 paragraphs where the word appears,
    sorted by how many times it appears in each paragraph.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        word = request.query_params.get("word", "").lower()
        if not word:
            return Response({"error": "Please provide a word to search."}, status=status.HTTP_400_BAD_REQUEST)

        # Filter WordMapping for this word
        results = (
            WordMapping.objects.filter(word=word)
            .values("paragraph__id", "paragraph__text")
            .annotate(word_occurrences=Count("id"))
            .order_by("-word_occurrences")[:10]
        )

        return Response({
            "results": [
                {
                    "id": item["paragraph__id"],
                    "text": item["paragraph__text"],
                    "word_occurrences": item["word_occurrences"]
                }
                for item in results
            ]
        }, status=status.HTTP_200_OK)
