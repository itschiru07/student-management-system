# Student Management System (SMS)

A full-stack, responsive Student Management System built using a **Django REST Framework** backend and a modern **React + Vite** frontend. The application features user authentication via JWT tokens, protected routes, a full-featured administration dashboard, and complete Student CRUD operations.

---

## 🌟 Features

### 🔒 Backend (Django REST Framework)
* **Custom User Model**: Extended authentication system managing custom users and profiles.
* **REST APIs**: Structured API endpoints for student listing, detailed views, creation, updates, and deletion (CRUD).
* **JWT Authentication**: Secure token-based session handling using SimpleJWT (`/api/token/` and `/api/token/refresh/`).
* **CORS Management**: Fully configured `django-cors-headers` to enable safe communication with the Vite frontend.
* **Admin Dashboard**: Default Django Admin Panel configured to view database tables.

### 💻 Frontend (React + Vite)
* **Authentication Context**: Centralized auth state managing logins, logouts, and token validation dynamically.
* **Protected Routes**: Custom Route Guards (`ProtectedRoute`) preventing unauthenticated access to system dashboard pages.
* **Dashboard Layout**: Fully structured layout containing a top Navbar, collapsible Sidebar, and responsive main view.
* **Student CRUD**: User-friendly pages to list all students, view individual profiles, add new records, and edit existing information.
* **Bootstrap Styling**: Clean, modern component styling using Bootstrap 5.

---

## 🛠️ Tech Stack

* **Backend**: Python 3.14+, Django 6.0+, Django REST Framework, SimpleJWT, Pillow (Image Handling), SQLite.
* **Frontend**: React 19, Vite 8, React Router DOM 7, Axios, Bootstrap 5.
* **Database**: SQLite3.

---

## 📂 Project Structure

```text
sms-main/
│
├── Python1/                               # Django Backend Project
│   ├── accounts/                          # App managing users, custom profiles, and authentication
│   ├── api/                               # REST API serialization, views, and routes
│   ├── students/                          # App handling Student database schemas and logic
│   ├── student_management/                # Core Django configuration (settings, main URLs)
│   ├── templates/                         # HTML templates (fallback views)
│   ├── manage.py                          # Django CLI entrypoint
│   └── db.sqlite3                         # SQLite Database
│
├── student-management-frontend/           # React Frontend App
│   ├── src/
│   │   ├── api/                           # Axios configuration & interceptors
│   │   ├── assets/                        # Static assets (images/logos)
│   │   ├── components/                    # Reusable views (Navbar, Sidebar, Pages)
│   │   ├── context/                       # Auth Context Provider
│   │   ├── Layouts/                       # Standard layout wrappers
│   │   ├── routes/                        # Protected route guards
│   │   ├── App.jsx                        # Main Application router
│   │   └── main.jsx                       # React entrypoint
│   ├── index.html                         # SPA base HTML
│   ├── package.json                       # npm configurations and dependencies
│   └── vite.config.js                     # Vite build configuration
│
└── .gitignore                             # Ignored files (node_modules, db.sqlite3, cash, etc.)
```

---

## 🚀 Installation & Running Guide

Ensure you have **Python 3** and **Node.js (v18+)** installed.

### 1. Backend Setup (Django)

From the root project directory (`sms-main`), open a terminal and run the following:

1. **Install Python dependencies**:
   ```bash
   py -m pip install django django-cors-headers djangorestframework djangorestframework-simplejwt Pillow
   ```

2. **Apply migrations**:
   ```bash
   py Python1/manage.py migrate
   ```

3. **Start the development server**:
   ```bash
   py Python1/manage.py runserver
   ```
   *The backend will run on `http://127.0.0.1:8000/`*

---

### 2. Frontend Setup (React)

Open a second terminal window from the root project directory (`sms-main`) and run the following:

1. **Navigate to the frontend directory**:
   ```bash
   cd student-management-frontend
   ```

2. **Install node dependencies**:
   ```bash
   npm install
   ```

3. **Start the development server**:
   ```bash
   npm run dev
   ```
   *The frontend will run on `http://localhost:5173/`*

---

## 🔒 API Endpoints

| Method | Endpoint | Description | Auth Required |
|---|---|---|---|
| **POST** | `/api/token/` | Obtain JWT token pair (Access/Refresh) | No |
| **POST** | `/api/token/refresh/` | Refresh expired access token | No |
| **GET** | `/api/students/` | Get list of all students | Yes |
| **POST** | `/api/students/` | Create a new student record | Yes |
| **GET** | `/api/students/<id>/` | Get detailed record of a single student | Yes |
| **PUT** | `/api/students/<id>/` | Edit/Update a student record | Yes |
| **DELETE** | `/api/students/<id>/` | Delete a student record | Yes |
