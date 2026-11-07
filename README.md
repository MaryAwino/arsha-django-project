# Arsha Website — Django Web Application

A responsive website built by converting the Arsha HTML template into a Django web application. The project combines frontend technologies with Django backend functionality to handle contact messages and newsletter subscriptions.

## Project Overview

The purpose of this project was to transform a static HTML website into a functional Django application while maintaining the original Arsha design and layout.

Django provides the backend functionality, processes form submissions and stores submitted information in an SQLite database.

## Features

- Responsive homepage based on the Arsha template.
- Reusable Django base template and template inheritance.
- Blog page.
- Navigation between website sections.
- Portfolio category filtering.
- Functional contact form.
- Contact messages stored in the database.
- Functional homepage and footer newsletter forms.
- Newsletter subscriptions stored in the database.
- Django Admin interface for managing contact messages and subscribers.
- Success notifications after form submissions.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Django | Web application framework |
| HTML5 | Website structure |
| CSS3 | Styling |
| JavaScript | Interactive functionality |
| Bootstrap | Responsive design |
| SQLite | Database |
| Git | Version control |
| GitHub | Source code hosting |

## Project Structure

```text
arsha-django-project/
│
├── config/                 # Django project configuration
├── website/                # Main Django application
│   ├── migrations/         # Database migrations
│   ├── static/             # CSS, JavaScript, images and vendor files
│   ├── templates/          # HTML templates
│   ├── admin.py            # Django Admin configuration
│   ├── models.py           # Database models
│   ├── urls.py             # Application URL patterns
│   └── views.py            # Application views
│
├── docs/
│   └── walkthrough.md      # Detailed project walkthrough
│
├── .gitignore
├── manage.py
└── README.md
```

## Getting Started

Follow these instructions to run the project locally.

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate into the project directory

```bash
cd arsha-django-project
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install Django

```bash
pip install django==6.1.3
```

### 6. Apply database migrations

```bash
python manage.py migrate
```

### 7. Create an administrator account (optional)

```bash
python manage.py createsuperuser
```

Follow the prompts to create your username and password.

### 8. Start the development server

```bash
python manage.py runserver
```

### 9. Open the website

Visit:

http://127.0.0.1:8000/

To access Django Admin:

http://127.0.0.1:8000/admin/

## Database Models

The application contains two main database models:

**ContactMessage**

Stores messages submitted through the contact form.

Fields:
- Name
- Email
- Subject
- Message
- Date created

**NewsletterSubscription**

Stores email addresses submitted through the newsletter forms.

Fields:
- Email
- Subscription date

Both models are registered in Django Admin for administrative management.

## Project Documentation

A detailed explanation of the development process, from initial Django setup to testing the completed website, is available in:

[`docs/walkthrough.md`](docs/walkthrough.md)

## Testing

The following functionality was tested locally:

- Homepage and blog page loading.
- Navigation and section scrolling.
- Portfolio filtering.
- Contact form submissions.
- Saving contact messages to SQLite.
- Homepage newsletter subscriptions.
- Footer newsletter subscriptions.
- Saving newsletter records.
- Viewing records through Django Admin.
- JavaScript functionality and browser console errors.

## Future Improvements

Possible future enhancements include:

- Dynamic blog management through Django Admin.
- Improved form validation.
- Email notifications for contact submissions.
- Production deployment.
- Additional security and performance improvements.

## Acknowledgements

The frontend design is based on the Arsha HTML template by BootstrapMade.

This project was developed as a practical exercise in integrating frontend web technologies with Python and Django.

---

**Project:** Arsha Django Website  
**Framework:** Django  
**Status:** Local development version completed and tested.
