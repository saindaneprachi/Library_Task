# Library_Task

# Library Management System

This is a simple Library Management System built with **Django**, **Django REST Framework**, and **JWT authentication**, allowing admin users to manage books and students to view available books.

##  Technologies Used
- Django 5.2
- Django REST Framework
- Simple JWT (Token Authentication)
- MySQL Database
- Django Templates (for basic UI)

## Features

### Admin (via API & UI):
- Sign Up
- Login (JWT token)
- Add, View, Update, Delete Books

### Student (via UI):
- View all available books


## Authentication

Admin users must log in via JWT:
- Obtain token: `POST /api/token/`
- Refresh token: `POST /api/token/refresh/`

Use these tokens to access authenticated endpoints (like book CRUD).

## Setup Instructions

### Prerequisites
- Python 3.10
- MySQL Server
- pipenv / virtualenv
- `PyMySQL`

### 1. Clone the Repository

git clone https://github.com/your-username/Library_Task.git
cd Library_Task

### 2. Create Virtual Environment & Install Dependencies

python -m venv my_env
source my_env/bin/activate  
pip install -r requirements.txt


### 3. Set db credentials i have used .env

### 4. Runmigrations
python manage.py makemigrations
python manage.py migrate


### 5. Runsever
python3 manage.py runserver


### 6.And Points
POST     api/token/                 to generate token,
POST	/admin/signup/	              Admin Signup,
GET	    /admin/books/	List          Books (admin),
POST	/admin/books/	                Add Book,
PUT	    /admin/books/{id}/        	Update Book,
DELETE	/admin/books/{id}/	        Delete Book,
GET	    admin/student/books/	      Student book list UI
