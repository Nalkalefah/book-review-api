# book-review-api# Book Review API

## Project Description
This project is a RESTful API built using Django REST Framework (DRF).

The system allows users to:
- Register and login using JWT authentication
- Browse books
- Add reviews to books
- Edit or delete their own reviews

Admin users can create, update, and delete books.

---

## Technologies Used
- Python 3
- Django
- Django REST Framework
- Simple JWT Authentication
- SQLite3
- Postman

---

## Installation

Install requirements:
pip install django
pip install djangorestframework
pip install djangorestframework-simplejwt

Run migrations:
python manage.py makemigrations
python manage.py migrate

Run server:
python manage.py runserver

---

## API Endpoints

### Authentication
- POST /api/register/
- POST /api/token/
- POST /api/token/refresh/

### Books
- GET /api/books/
- GET /api/books/<id>/
- POST /api/books/
- PUT /api/books/<id>/
- DELETE /api/books/<id>/

### Reviews
- POST /api/books/<book_id>/reviews/
- GET /api/books/<book_id>/reviews/
- PUT /api/reviews/<id>/
- DELETE /api/reviews/<id>/

---

## Authentication
JWT Authentication is used in this project.

Users must obtain an access token using:
POST /api/token/

Then include the token in Authorization header:
Bearer <access_token>

---

## Testing
API endpoints were tested using Postman.
