# User CRUD Project (Django + Streamlit)

A full-stack CRUD application built with Django REST Framework and Streamlit.

The project provides REST APIs for managing user profiles and a Streamlit-based dashboard to perform Create, Read, Update, and Delete (CRUD) operations through a simple web interface.

Tech Stack
Backend: Python, Django, Django REST Framework
Frontend: Streamlit
Database: SQLite
API: REST API
Environment: Python Virtual Environment

## Project Structure

```text
user-crud-backend/
│
├── backend/
│   ├── config/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── asgi.py
│   │   └── wsgi.py
│   │
│   ├── users/
│   │   ├── migrations/
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   └── ...
│   │
│   ├── venv/
│   │
│   ├── create_admin_user.py
│   ├── db.sqlite3
│   ├── db.sqlite3.bak
│   ├── manage.py
│   ├── repair_manage.py
│   └── requirement.txt
│
├── frontend/
│   ├── __pycache__/
│   └── streamlit_app.py
│
└── README.md
```

### Backend

The `backend/` directory contains the Django REST API.

* `config/` — Django project configuration and settings
* `users/` — UserProfile model, serializers, views, URLs, and migrations
* `manage.py` — Django management utility
* `create_admin_user.py` — Script for creating an admin user
* `repair_manage.py` — Utility script for repairing the Django management setup
* `requirement.txt` — Python dependencies
* `db.sqlite3` — SQLite database used for local development
* `db.sqlite3.bak` — Database backup file
* `venv/` — Python virtual environment used for local development

### Frontend

The `frontend/` directory contains the Streamlit dashboard.

* `streamlit_app.py` — Streamlit application that communicates with the Django REST API
* `__pycache__/` — Python-generated cache files

Features
Create a new user profile
View all users
View individual user details
Update user information
Delete user profiles
Django Admin interface for managing users
Streamlit dashboard for interacting with the APIs
SQLite database for local data storage

API Endpoints
Users
Method	Endpoint	Description
GET	/api/users/	Get all users
POST	/api/users/	Create a new user
GET	/api/users/<id>/	Get a specific user
DELETE	/api/users/<id>/	Delete a user
Setup
1. Clone the Repository
git clone https://github.com/snehasahu04/user-crud-backend.git
cd user-crud-backend
2. Create a Virtual Environment

From the backend directory:
cd backend
python -m venv venv

Activate the virtual environment:

.\venv\Scripts\Activate.ps1
3. Install Dependencies
python -m pip install -r requirement.txt
4. Apply Database Migrations
python manage.py makemigrations
python manage.py migrate
5. Create an Admin User
python manage.py createsuperuser

Follow the prompts to create the Django admin account.

Run the Backend

Start the Django development server:

python manage.py runserver

The backend will be available at:

http://127.0.0.1:8000/
Run the Streamlit Dashboard

Open another terminal, activate the virtual environment, and run:

cd C:\user_crud_project\backend
.\venv\Scripts\Activate.ps1
streamlit run ..\frontend\streamlit_app.py

The Streamlit dashboard will be available at:

http://localhost:8501
Django Admin

The Django Admin interface can be accessed at:

http://127.0.0.1:8000/admin/

It can be used to view and manage user profiles directly from the Django administration panel.

Database

The project uses SQLite for local development.

Database file:

backend/db.sqlite3
Application Flow
Streamlit Dashboard
        │
        ▼
Django REST API
        │
        ▼
UserProfile Model
        │
        ▼
SQLite Database

The Streamlit frontend sends HTTP requests to the Django REST API. Django processes the request through the API layer and performs the required operation on the SQLite database.

CRUD Operations

The application supports the complete CRUD workflow:

Create  →  Add a new user
Read    →  View existing users
Update  →  Modify user information
Delete  →  Remove a user
Running the Project Locally

Start Django first:

python manage.py runserver

Then start Streamlit in a separate terminal:

streamlit run frontend/streamlit_app.py

Both services need to be running for the Streamlit dashboard to communicate with the Django API.

Troubleshooting
DELETE request returns "Method DELETE not allowed"

Make sure you are using the detail endpoint with the user ID:

/api/users/<id>/

For example:

http://127.0.0.1:8000/api/users/1/
Streamlit installation issues

If package installation fails, upgrade the Python packaging tools:

python -m pip install --upgrade pip setuptools wheel

Then install the project requirements again:

python -m pip install -r requirement.txt
Future Improvements
Add authentication and authorization
Add form validation
Improve the Streamlit dashboard UI
Add pagination and search functionality
Add automated API tests
Deploy the application to a cloud platform
