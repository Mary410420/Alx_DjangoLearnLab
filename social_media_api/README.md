# Social Media API

A simple **Django REST Framework** API for a social media platform with **user authentication** and profile management.

---

## Features

- User registration
- User login with token authentication
- Profile retrieval and update
- Followers (Many-to-Many relationship)
- Secure password hashing

---

## Tech Stack

- Python 3.x
- Django 4.x
- Django REST Framework
- Django REST Framework Token Authentication
- SQLite (default) / Optional: PostgreSQL for production

---

## Setup Instructions

### 1. Clone the repository

    ```bash
    git clone <YOUR_REPO_URL>
    cd social_media_api



### 2. Create a virtual environment
    ```bash
    python -m venv venv
    .\venv\Scripts\Activate.ps1   # Windows PowerShell



### 3. Install dependencies
    ```bash
    pip install -r requirements.txt
If you don’t have requirements.txt, install manually:
    ```bash
    pip install django djangorestframework djangorestframework-simplejwt Pillow

### 4. Apply migrations
    ```bash
    python manage.py makemigrations
    python manage.py migrate

### 5. Create a superuser (optional)
    ```bash
    python manage.py createsuperuser


### 6. Run the development server
    ```bash
    python manage.py runserver



### Example Requests (PowerShell)
```bash
API Endpoints
Endpoint	Method	Description
/api/accounts/register/	POST	Register a new user
/api/accounts/login/	POST	Login and get token
/api/accounts/profile/	GET	Retrieve your profile (requires token)
/api/accounts/profile/	PUT	Update your profile (requires token)



Example Requests (PowerShell)
Register
Invoke-RestMethod -Method POST `
  -Uri "http://127.0.0.1:8000/api/accounts/register/" `
  -Headers @{ "Content-Type" = "application/json" } `
  -Body '{"username": "testuser", "email": "test@example.com", "password": "password123"}'

Login
Invoke-RestMethod -Method POST `
  -Uri "http://127.0.0.1:8000/api/accounts/login/" `
  -Headers @{ "Content-Type" = "application/json" } `
  -Body '{"username": "testuser", "password": "password123"}'

Get Profile
Invoke-RestMethod -Method GET `
  -Uri "http://127.0.0.1:8000/api/accounts/profile/" `
  -Headers @{ "Authorization" = "Token YOUR_TOKEN_HERE" }

Update Profile
Invoke-RestMethod -Method PUT `
  -Uri "http://127.0.0.1:8000/api/accounts/profile/" `
  -Headers @{ "Content-Type" = "application/json"; "Authorization" = "Token YOUR_TOKEN_HERE" } `
  -Body '{"bio": "Hello world!", "email": "newemail@example.com"}'