# Codemonk Backend Assignment

This project is a backend assignment built with **Django** and **Django REST Framework**. It supports:
- User registration & login using JWT
- Uploading paragraphs
- Searching words across stored paragraphs
- Mapping words to paragraph IDs

---

## 🚀 Tech Stack

- Python 3
- Django
- Django REST Framework
- PostgreSQL (or SQLite as fallback)
- JWT Authentication
- Postman (for API testing)

---

## 🔧 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/shantanuraut-codes/codemonk-backend.git
cd codemonk-backend
```

### 2. Create Virtual Environment (optional)

```bash
python3 -m venv env
source env/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Migrations

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

### 5. Create Superuser (for admin access)

```bash
python3 manage.py createsuperuser
```

### 6. Run the Server

```bash
python3 manage.py runserver
```

Now visit:  
`http://127.0.0.1:8000/admin/` (Admin panel)  
`http://127.0.0.1:8000/api/` (API root)

---

## 🔐 Authentication

### ✅ Register

**POST** `/api/register/`  
Body (JSON):

```json
{
  "username": "testuser",
  "password": "testpass123"
}
```

### 🔑 Get JWT Token

**POST** `/api/token/`  
Body:

```json
{
  "username": "testuser",
  "password": "testpass123"
}
```

Response will include `access` and `refresh` tokens.

### 🛂 Auth Headers for Secure Routes

In Postman, add:

```
Key: Authorization
Value: Bearer <access_token>
```

---

## 📄 API Usage

### 1. Upload Paragraph

**POST** `/api/paragraphs/`  
Header: `Authorization: Bearer <token>`  
Body:

```json
{
  "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
}
```

### 2. Search Word

**GET** `/api/search/?word=lorem`  
Header: `Authorization: Bearer <token>`

### 3. Get All Word Mappings

**GET** `/api/word-mappings/`  
Header: `Authorization: Bearer <token>`

---

## 🧪 Testing with Postman

1. Register a user.
2. Login to get JWT tokens.
3. Add token to `Authorization` header in Bearer format.
4. Test uploading paragraphs and searching words.

---

## 📂 Folder Structure

```
codemonk-backend/
├── api/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
├── codemonk_backend/
│   ├── settings.py
├── db.sqlite3
├── manage.py
└── requirements.txt
```

---

## ✅ Final Notes

- Ensure migrations are applied.
- Always add the JWT token for protected endpoints.
- Admin panel helps verify entries visually.

---

**Shantanu Raut**  


