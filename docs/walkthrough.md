# Arsha Website — Django Conversion Walkthrough

## 1. Project Overview

This project involved converting the Arsha HTML website template into a Django web application.

The original template was built using HTML, CSS, JavaScript, Bootstrap and other frontend libraries. Django was introduced to provide backend functionality, handle form submissions, and store information in a database.

The main objective was to transform a static website into a functional Django application while retaining the original Arsha design and user experience.

## 2. Technologies Used

- **Python 3.12** — Backend programming language.
- **Django 6.1.3** — Python web framework.
- **HTML5** — Website structure.
- **CSS3** — Website styling.
- **JavaScript** — Interactive website functionality.
- **Bootstrap** — Responsive layout and components.
- **SQLite** — Development database.
- **Visual Studio Code** — Development environment.
- **Git and GitHub** — Version control and project hosting.

## 3. Project Setup

### Step 1: Create the project directory

A project folder named `arsha-django-project` was created to hold the Django application and its related files.

### Step 2: Create a Python virtual environment

A virtual environment named `venv` was created to isolate the project's Python dependencies.

The environment was activated before installing Django and running the application.

### Step 3: Install Django

Django was installed using Python's package installer:

```bash
pip install django
```

The installed Django version was 6.1.3.

### Step 4: Create the Django project

The Django project was created using:

```bash
django-admin startproject config .
```

The project configuration was stored in the `config` directory.

### Step 5: Create the website application

A Django application named `website` was created:

```bash
python manage.py startapp website
```

The `website` application contains the main website views, models, URLs, templates and static assets.

### Step 6: Register the application

The `website` application was added to `INSTALLED_APPS` in `config/settings.py` so Django could recognize and manage it.

## 4. Converting the Arsha HTML Template

The original Arsha template was used as the frontend foundation.

Its HTML pages were converted into Django templates.

### Step 1: Organize the templates

The following template files were created:

```text
website/
└── templates/
    └── website/
        ├── base.html
        ├── index.html
        └── blog.html
```

### Step 2: Create the base template

The `base.html` file contains the common website structure, including:

- HTML document structure.
- Navigation bar.
- Footer.
- Stylesheets.
- JavaScript files.
- Shared website components.

Django template inheritance was used to avoid repeating the same layout across pages.

### Step 3: Use template inheritance

The homepage and blog page extend the shared base template.

For example:

```django
{% extends 'website/base.html' %}
{% load static %}
```

Content specific to each page is placed inside Django template blocks.

### Step 4: Configure static files

The original Arsha CSS, JavaScript, images and vendor libraries were copied into:

```text
website/static/website/
```

The static directory contains:

```text
static/website/
├── css/
├── img/
├── js/
└── vendor/
```

Django's static template tag was used to load these files:

```django
{% load static %}
```

Example:

```django
<script src="{% static 'website/js/main.js' %}"></script>
```

This allows Django to locate and serve the website's static assets during development.

## 5. Configure Django URLs and Views

### Step 1: Configure the main URLs

The main URL configuration was updated in `config/urls.py` to include the website application's URL patterns.

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
]
```

### Step 2: Create website URL patterns

The following routes were configured in `website/urls.py`:

- `/` — Homepage.
- `/blog.html` — Blog page.
- `/contact.html` — Contact form endpoint.
- `/newsletter/` — Newsletter subscription endpoint.

### Step 3: Create views

The corresponding views were implemented in `website/views.py`.

The homepage and blog views render their respective Django templates.

The contact and newsletter views process submitted form data and interact with the database.

## 6. Implementing the Contact Form

The original contact form was converted into a Django-powered form.

### Step 1: Create the ContactMessage model

A model named `ContactMessage` was created in `website/models.py`.

It contains:

- `name` — Name of the sender.
- `email` — Sender's email address.
- `subject` — Message subject.
- `message` — Message content.
- `created_at` — Date and time the message was received.

### Step 2: Configure the database

Django migrations were created and applied to generate the database table.

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 3: Connect the contact form to Django

The contact form was configured to submit using the POST method.

Django's CSRF protection was added:

```django
{% csrf_token %}
```

The form submits to the Django contact URL.

### Step 4: Process contact submissions

The contact view retrieves the submitted information using `request.POST`.

It creates a new `ContactMessage` database record and displays a success message after submission.

### Step 5: Test the contact form

The form was tested through the website.

Submitted messages were successfully saved and could be viewed through Django Admin.

## 7. Implementing the Newsletter Subscription

The newsletter forms were also converted into Django-powered forms.

### Step 1: Create the NewsletterSubscription model

A model named `NewsletterSubscription` was created.

It contains:

- `email` — Subscriber's email address.
- `subscribed_at` — Date and time of subscription.

The email field was configured as unique to prevent duplicate subscriptions.

### Step 2: Create the newsletter view

The newsletter view retrieves the submitted email address.

It uses Django's `get_or_create()` method to create a subscription only when the email does not already exist.

### Step 3: Configure the newsletter URL

The `/newsletter/` route was connected to the newsletter view.

### Step 4: Update the newsletter forms

Both the homepage newsletter form and footer newsletter form were connected to the Django endpoint.

CSRF protection was included in both forms.

### Step 5: Test newsletter submissions

The newsletter forms were tested successfully.

Submitted email addresses were saved in the database and displayed in Django Admin.

A success message was also displayed after subscription.

## 8. Django Admin Configuration

Django Admin was configured to make it easier to manage submitted contact messages and newsletter subscriptions.

The two models were registered in `website/admin.py`.

The admin interface was customized to display useful information.

For contact messages, the interface includes:

- Sender's name.
- Email address.
- Subject.
- Submission date.
- Search and filtering options.

For newsletter subscriptions, it includes:

- Subscriber email.
- Subscription date.
- Search functionality.
- Ordering by most recent subscriptions.

This makes it possible for an administrator to review information stored by the application.

## 9. Fixing JavaScript Dependencies

During testing, some JavaScript errors appeared in the browser console because certain Arsha vendor libraries were not loaded.

The following dependencies were identified and added to `base.html`:

- Waypoints.
- imagesLoaded.
- Isotope Layout.

The scripts were loaded before the main Arsha JavaScript file.

After adding the missing dependencies, the website was refreshed and the browser console was checked again.

The JavaScript errors were resolved.

The following functionality was also tested:

- Navigation links and section scrolling.
- Portfolio category filtering.
- Website interactive elements.

## 10. Testing the Application

The application was run locally using Django's development server:

```bash
python manage.py runserver
```

The website was accessed through:

```text
http://127.0.0.1:8000/
```

The following functionality was tested:

1. Homepage loads correctly.
2. Website navigation works.
3. Blog page opens.
4. Portfolio category filtering works.
5. Contact form accepts submissions.
6. Contact messages are saved in the database.
7. Homepage newsletter form works.
8. Footer newsletter form works.
9. Newsletter subscriptions are saved.
10. Django Admin displays submitted records.
11. Success messages are displayed after successful form submissions.

## 11. Final Project Structure

The project is organized as follows:

```text
arsha-django-project/
│
├── config/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── website/
│   ├── migrations/
│   ├── static/
│   │   └── website/
│   │       ├── css/
│   │       ├── img/
│   │       ├── js/
│   │       └── vendor/
│   │
│   ├── templates/
│   │   └── website/
│   │       ├── base.html
│   │       ├── index.html
│   │       └── blog.html
│   │
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── docs/
│   └── walkthrough.md
│
├── .gitignore
├── manage.py
└── README.md
```

## 12. Key Learning Outcomes

Through this project, I gained practical experience in:

- Creating and configuring a Django project.
- Understanding Django applications and project structure.
- Converting static HTML pages into Django templates.
- Using template inheritance to reuse website components.
- Configuring static files.
- Creating Django views and URL routes.
- Designing database models.
- Running migrations.
- Processing POST requests.
- Implementing CSRF protection.
- Saving form submissions in SQLite.
- Managing application data through Django Admin.
- Debugging JavaScript dependencies.
- Testing website functionality.
- Using Git and GitHub for version control.

## 13. Conclusion

This project demonstrates how a static HTML website can be converted into a Django web application while retaining its original frontend design.

Django was used to introduce backend functionality, including contact message management and newsletter subscriptions.

The project provided practical experience in integrating frontend technologies with Python and Django, managing application data, troubleshooting dependencies and organizing a web development project.

**Project status:** Local development version completed and tested. Further improvements, such as dynamic blog management and production deployment, can be implemented in future development stages.
