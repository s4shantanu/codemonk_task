from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.ParagraphUploadView.as_view(), name='upload'),
    path('search/', views.WordSearchView.as_view(), name='search'),
]
