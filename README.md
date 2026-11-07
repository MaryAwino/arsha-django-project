# Arsha Website — Django Web Application

A responsive website built by converting the Arsha HTML template into a functional Django web application. The project combines frontend technologies with Django backend functionality, including contact messages, newsletter subscriptions, and a dynamic blog management system.

## Project Overview

The purpose of this project was to transform a static HTML website into a functional Django application while maintaining the original Arsha design and layout.

Django provides the backend functionality, processes form submissions, manages blog content, handles image uploads, and stores application data in an SQLite database.

## Features

- Responsive homepage based on the Arsha template.
- Reusable Django base template and template inheritance.
- Navigation between website sections.
- Portfolio category filtering.
- Functional contact form.
- Contact messages stored in the database.
- Functional homepage and footer newsletter forms.
- Newsletter subscriptions stored in the database.
- Django Admin interface for managing contact messages and subscribers.
- Dynamic blog post management through Django Admin.
- Create, edit, and delete blog posts.
- Publish and unpublish blog posts.
- Dynamic blog listing displaying published articles.
- Individual blog detail pages.
- Dynamic Recent Posts sidebar.
- Featured image uploads for blog posts.
- Uploaded images stored in the media directory.
- Success notifications after form submissions.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Django 6.1.3 | Web application framework |
| Pillow | Image processing and uploads |
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
├── config/                  # Django project configuration
├── website/                 # Main Django application
│   ├── migrations/          # Database migrations
│   ├── static/              # CSS, JavaScript, images and vendor files
│   ├── templates/           # HTML templates
│   │   └── website/
│   │       ├── base.html
│   │       ├── index.html
│   │       ├── blog.html
│   │       └── blog-detail.html
│   ├── admin.py             # Django Admin configuration
│   ├── models.py            # Database models
│   ├── urls.py              # Application URL patterns
│   └── views.py             # Application views
│
├── media/                   # Uploaded media files (created locally)
├── docs/
│   └── walkthrough.md       # Detailed project walkthrough
│
├── requirements.txt
├── .gitignore
├── manage.py
└── README.md
```

The `media/` directory is used for uploaded blog images. It is created locally when media files are uploaded.

## Getting Started

Follow these instructions to run the project locally.

### 1. Clone the repository

```bash
git clone https://github.com/MaryAwino/arsha-django-project.git
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

### 5. Install project dependencies

```bash
pip install -r requirements.txt
```

### 6. Apply database migrations

```bash
python manage.py migrate
```

### 7. Create an administrator account

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

The application contains three main database models.

### ContactMessage

Stores messages submitted through the contact form.

Fields:
- Name
- Email
- Subject
- Message
- Date created

### NewsletterSubscription

Stores email addresses submitted through the newsletter forms.

Fields:
- Email
- Subscription date

### BlogPost

Stores blog articles managed through Django Admin.

Fields:
- Title
- Slug
- Author
- Featured image
- Excerpt
- Content
- Published status
- Date created
- Date updated

The `published` field controls whether an article is visible on the public website.

All three models are registered in Django Admin for administrative management.

## Blog Management

Blog content can be managed through the Django Admin interface.

Administrators can:

- Create new blog posts.
- Edit existing articles.
- Upload featured images.
- Publish or unpublish articles.
- Manage article content and excerpts.

Only published articles appear on the public blog page.

Each published article has an individual detail page accessible through its unique slug.

## Media and Image Uploads

Django media settings are configured to handle uploaded blog images during local development.

- `MEDIA_URL` defines the URL used to access uploaded media.
- `MEDIA_ROOT` defines the directory where uploaded files are stored.
- Pillow provides image-processing support.

Uploaded blog images are stored in:

```text
media/blog_images/
```

For production deployment, media files should be served using an appropriate web server or cloud storage service.

## Project Documentation

A detailed explanation of the development process, from initial Django setup to the implementation of the website's functionality, is available in:

[docs/walkthrough.md](docs/walkthrough.md)

## Testing

The following functionality has been tested locally:

- Homepage and blog page loading.
- Navigation and section scrolling.
- Portfolio filtering.
- Contact form submissions.
- Saving contact messages to SQLite.
- Homepage newsletter subscriptions.
- Footer newsletter subscriptions.
- Saving newsletter records.
- Viewing records through Django Admin.
- Creating and managing blog posts through Django Admin.
- Publishing and hiding blog posts.
- Displaying published articles dynamically.
- Opening individual blog detail pages.
- Uploading and displaying featured images.
- Django system checks.
- JavaScript functionality and browser console errors.

## Future Improvements

Possible future enhancements include:

- Improved form validation.
- Email notifications for contact submissions.
- Blog search functionality.
- Functional blog pagination.
- Production deployment.
- Additional security and performance improvements.

## Acknowledgements

The frontend design is based on the Arsha HTML template by BootstrapMade.

This project was developed as a practical exercise in integrating frontend web technologies with Python and Django.

---

**Project:** Arsha Django Website  
**Framework:** Django  
**Status:** Local development version completed and tested.
