# Student Management System

A simple and clean **Student Management System** built with **Django**. This project allows users to manage student records through a web-based interface with CRUD (Create, Read, Update, Delete) functionality.

## Features

* Add new students
* View all students
* Update student information
* Delete students with confirmation
* Form validation using Django ModelForms
* Unique email validation
* Responsive and clean user interface
* SQLite database for development

## Tech Stack

* **Python**
* **Django**
* **HTML**
* **Tailwind CSS**
* **SQLite**
* **Git & GitHub**

## Project Structure

```text
student-management/
│
├── StudentManagement/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── students/
│   ├── migrations/
│   ├── templates/
│   │   └── students/
│   │       ├── student_list.html
│   │       ├── student_form.html
│   │       └── student_delete.html
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── .gitignore
├── manage.py
└── README.md
```

## Student Model

The application currently stores the following student information:

* Name
* Email
* Age
* Address
* Created date

The email field is configured to be unique to prevent duplicate student records.

## CRUD Functionality

The application follows the standard CRUD operations:

| Operation | Description                         |
| --------- | ----------------------------------- |
| Create    | Add a new student                   |
| Read      | View all students                   |
| Update    | Edit existing student information   |
| Delete    | Remove a student after confirmation |

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/student-management.git
cd student-management
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
```

### 3. Activate the virtual environment

Linux/macOS:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install django
```

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Start the development server

```bash
python manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/students/
```

## Important

Environment variables and sensitive files such as `.env`, the virtual environment, and the local SQLite database are excluded from version control through `.gitignore`.

## Learning Goals

This project was created to practice and understand Django fundamentals, including:

* Django project and app structure
* Models and database relationships
* Django ORM
* ModelForms
* URL routing
* Views
* Templates
* CRUD operations
* Form validation
* Django migrations
* Git and GitHub workflow

## Future Improvements

Some possible future additions include:

* User authentication
* Student search and filtering
* Pagination
* Course management
* Teacher management
* Dashboard and statistics
* REST API integration
* PostgreSQL database
* Improved UI and accessibility
