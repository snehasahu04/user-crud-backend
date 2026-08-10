# User CRUD Project (Django + Streamlit)

Simple Django backend providing CRUD APIs for `UserProfile` and a Streamlit frontend dashboard.

## Repo layout

- `backend/` - Django project (models, APIs, db.sqlite3)
- `frontend/` - Streamlit dashboard (`streamlit_app.py`)

## Requirements

- Python 3.13 (used here)
- A virtual environment is recommended

## Setup (Windows / PowerShell)

1. Open PowerShell and go to the backend folder:

```powershell
cd C:\user_crud_project\backend
```

2. Create and activate a venv (if you haven't already):

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

3. Install requirements:

```powershell
python -m pip install -r requirement.txt
```

4. Apply migrations:

```powershell
python manage.py makemigrations
python manage.py migrate
```

5. Create admin user (example):

```powershell
# Interactive (recommended):
python manage.py createsuperuser

# Or use the provided default created during setup in this workspace:
Username: admin
Password: Admin@123
```

6. Run the Django dev server:

```powershell
python manage.py runserver
```

## Streamlit frontend

Make sure Django is running (step above), then in another terminal run:

```powershell
cd C:\user_crud_project\backend
.\venv\Scripts\Activate.ps1
streamlit run ..\frontend\streamlit_app.py
```

Open the dashboard at `http://localhost:8501`.

## API Endpoints

- List / Create: `GET/POST http://127.0.0.1:8000/api/users/`
- Retrieve / Update / Delete: `GET/PATCH/PUT/DELETE http://127.0.0.1:8000/api/users/<id>/`

Use the admin at `http://127.0.0.1:8000/admin/` to view and manage data.

## Where data is stored

The project uses SQLite by default. DB file:

```
backend/db.sqlite3
```

## Git / Push to GitHub (example commands)

If you haven't initialized a Git repo yet, run these from the workspace root (`C:\user_crud_project`):

```powershell
cd C:\user_crud_project
git init
git add .
git commit -m "Initial commit: Django backend + Streamlit frontend"
# create a remote repository on GitHub (via website) and copy the remote URL, then:
git remote add origin https://github.com/<your-username>/<your-repo>.git
git branch -M main
git push -u origin main
```

If you already have a remote, just add and push the branch:

```powershell
git add .
git commit -m "Update: backend + frontend"
git push
```

## Troubleshooting

- If `streamlit` install fails on Windows due to NumPy builds, upgrade `pip`, `setuptools`, and `wheel` and install a Streamlit release with prebuilt wheels for Python 3.13 (example used `streamlit==1.61.1`).
- If `DELETE` request returns `Method "DELETE" not allowed.`, ensure you are calling the detail endpoint with trailing slash: `/api/users/<id>/`.

## Next steps / Notes

- Add frontend UI pages or a React app in the `frontend/` folder if you prefer a single-page app.
- Remove any helper scripts that create users automatically, or rotate the admin password before sharing the repo publicly.

---
Happy coding!
