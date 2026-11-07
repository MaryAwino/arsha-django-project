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
- **Pillow 13.0.0** — Image processing and support for blog image uploads.

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

`website/
└── templates/
    └── website/
        ├── base.html
        ├── index.html
        ├── blog.html
        └── blog-detail.html
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

The following routes were configured in `website/urls.py`:

- `/` — Homepage.
- `/blog.html` — Blog listing page.
- `/blog/<slug>/` — Individual blog article.
- `/contact.html` — Contact form endpoint.
- `/newsletter/` — Newsletter subscription endpoint.

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

## 8. Implementing Dynamic Blog Management

The original blog page contained static, hardcoded article content. It was converted into a dynamic blog system using Django models, views, templates and Django Admin.

### Step 1: Create the BlogPost model

A `BlogPost` model was added to `website/models.py`.

The model contains:

- `title` — Blog article title.
- `slug` — Unique URL-friendly identifier.
- `author` — Name of the article author.
- `featured_image` — Uploaded article image.
- `excerpt` — Short article description.
- `content` — Full article content.
- `published` — Controls whether the article is publicly visible.
- `created_at` — Date and time the article was created.
- `updated_at` — Date and time the article was last updated.

### Step 2: Install Pillow

Pillow was installed to provide image-processing support for Django image uploads.

```bash
pip install Pillow
```

### Step 3: Create and apply migrations

Database migrations were generated and applied to create the `BlogPost` table.

```bash
python manage.py makemigrations website
python manage.py migrate
```

### Step 4: Register BlogPost in Django Admin

The `BlogPost` model was registered in `website/admin.py`.

The admin interface was customised to display article titles, authors, publication status and creation dates.

Search and filtering options were also configured.

The `prepopulated_fields` option was used to automatically generate article slugs from titles.

### Step 5: Create dynamic blog views

The blog listing view retrieves published articles from the database and orders them by creation date.

The individual blog detail view retrieves an article using its slug and displays its full content.

Unpublished articles are excluded from the public website.

### Step 6: Convert the blog template into a dynamic page

The original hardcoded blog articles were replaced with a Django template loop.

The template dynamically displays:

- Featured images.
- Article titles.
- Authors.
- Publication dates.
- Excerpts.
- Links to individual articles.

An empty-state message was added for situations where no published articles are available.

### Step 7: Create the individual article template

A `blog-detail.html` template was created.

It extends the shared `base.html` template and displays the selected article's title, author, date, featured image and full content.

A link back to the blog listing page was also included.

### Step 8: Make Recent Posts dynamic

The Recent Posts sidebar was connected to the database.

It retrieves the five most recent published articles and displays their titles, dates, images and links.

### Step 9: Test blog management

The following functionality was tested successfully:

- Creating a blog post through Django Admin.
- Editing and publishing an article.
- Hiding unpublished articles from public visitors.
- Displaying published articles on the blog listing page.
- Opening individual articles using their slugs.
- Displaying recent articles in the sidebar.

## 9. Configuring Media Files and Image Uploads

Django was configured to handle images uploaded through the BlogPost model.

### Step 1: Configure media settings

The following settings were added to `config/settings.py`:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

`MEDIA_URL` defines the URL used to access uploaded files, while `MEDIA_ROOT` specifies the directory where Django stores them.

### Step 2: Configure media URL patterns

The following imports were added to `config/urls.py`:

```python
from django.conf import settings
from django.conf.urls.static import static
```

Media URL patterns were then configured for development:

```python
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
```

This allows uploaded images to be served during local development.

### Step 3: Upload featured images

The featured image field was made available through Django Admin.

When an administrator uploads an image, Django stores it inside:

```text
media/
└── blog_images/
```

### Step 4: Display uploaded images

The blog listing and individual article templates were configured to display uploaded images using the image field's URL.

```django
{% if post.featured_image %}
    <img src="{{ post.featured_image.url }}" alt="{{ post.title }}">
{% endif %}
```

### Step 5: Test image uploads

An image was uploaded through Django Admin and successfully displayed on both the blog listing page and individual article page.

This confirmed that the media configuration and image upload functionality were working correctly.

**Note:** The media-serving configuration is intended for development. A production deployment requires an appropriate media storage and serving solution.

## 10. Django Admin Configuration

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

## 11. Fixing JavaScript Dependencies

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

## 12. Testing Application

After implementing the website features, the application was tested to confirm that the pages, forms, database operations and blog management functionality worked correctly.

### 12.1 Website Navigation

The following pages were tested:

- Homepage (`/`)
- Blog listing page (`/blog.html`)
- Individual blog article pages (`/blog/<slug>/`)
- Contact page (`/contact.html`)

The navigation links were checked to ensure that users could move between the website pages.

### 12.2 Static Files

The website's CSS, JavaScript, images and vendor libraries were tested to confirm that they loaded correctly.

The Bootstrap styling, animations, image displays and portfolio filtering functionality were also checked.

### 12.3 Contact Form

The contact form was tested by submitting sample information.

The submitted name, email, subject and message were successfully saved in the Django database.

### 12.4 Newsletter Subscription

The newsletter form was tested by submitting an email address.

The subscription was successfully saved in the database, and a confirmation message was displayed.

### 12.5 Django Admin

The Django Admin dashboard was tested to confirm that administrators could manage:

- Contact messages
- Newsletter subscriptions
- Blog posts

Blog posts could be created, edited, published and unpublished through the Admin dashboard.

### 12.6 Dynamic Blog Functionality

The blog functionality was tested by creating a sample blog post through Django Admin.

The following operations were confirmed:

- Published blog posts appeared on the blog listing page.
- Unpublished posts were not displayed publicly.
- Clicking a blog title opened its individual article page.
- The article title, author, publication date and content were displayed.
- Recent Posts were displayed dynamically in the blog sidebar.

### 12.7 Blog Image Uploads

A featured image was uploaded through Django Admin.

The image was successfully displayed on both the blog listing page and the individual blog article page.

### 12.8 Django System Check

The Django system check command was executed:

```bash
python manage.py check
```

The application returned:

```text
System check identified no issues (0 silenced).
```

This confirmed that Django did not detect any configuration or system-check errors at the time of testing.

## 13. Final Project Structure

The final project is organised as follows:

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
│   │   ├── __init__.py
│   │   ├── 0001_initial.py
│   │   ├── 0002_...py
│   │   └── 0003_blogpost.py
│   │
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
│   │       ├── blog.html
│   │       └── blog-detail.html
│   │
│   ├── __init__.py
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
├── media/
│   └── blog_images/
│       └── uploaded blog images
│
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

**Description of important directories and files:**

- `config/` — Contains the main Django project configuration.
- `website/` — Contains the website application, including models, views, URL patterns and admin configuration.
- `website/migrations/` — Contains database migration files used to manage changes to the database schema.
- `website/static/` — Stores the original Arsha CSS, JavaScript, images and vendor libraries.
- `website/templates/` — Contains the Django HTML templates.
- `media/` — Stores images uploaded through Django Admin.
- `docs/` — Contains the detailed project development walkthrough.
- `requirements.txt` — Lists the Python dependencies required to run the application.
- `manage.py` — Provides the Django command-line interface.
- `README.md` — Introduces the project and explains how to set it up.

**Note:** The migration filenames shown above illustrate the project structure. Keep the actual migration filenames generated in your project. The `media/` directory contains uploaded files locally and is not necessarily included in the GitHub repository.

## 14. Key Learning Outcomes

Through this project, I gained practical experience in developing a dynamic website using Python and Django.

The key skills and concepts I learned include:

1. **Django Project Structure:** Understanding how Django projects and applications are organised.
2. **Template Inheritance:** Creating a shared base template and extending it across multiple website pages.
3. **Static File Management:** Integrating CSS, JavaScript, images and third-party libraries into Django.
4. **URL Routing:** Connecting website URLs to the appropriate Django views.
5. **Django Views:** Processing requests and returning dynamic HTML pages.
6. **Database Models:** Creating models to store contact messages, newsletter subscriptions and blog posts.
7. **Database Migrations:** Applying model changes to the database using Django migrations.
8. **Django Forms and Data Handling:** Processing contact form submissions and newsletter subscriptions.
9. **Django Admin:** Managing website content and database records through the administration dashboard.
10. **Dynamic Content Management:** Displaying published blog posts and individual articles using database records.
11. **Image Uploads:** Using Django's `ImageField`, Pillow and media configuration to upload and display blog images.
12. **Git and GitHub:** Tracking project changes and maintaining project documentation.

The project strengthened my understanding of how frontend templates, backend logic and databases work together to create a functional web application.

## 15. Conclusion

The Arsha Django project provided an opportunity to transform a static HTML template into a dynamic website using Python and Django.

During development, I integrated the original Arsha design with Django's template system, configured static files, implemented contact and newsletter forms, and connected the application to an SQLite database.

I also developed a dynamic blog management system that allows administrators to create, edit, publish and manage blog posts through Django Admin. Featured image uploads and individual blog article pages were also implemented.

This project strengthened my practical understanding of Django, database management, backend development, template integration, media handling and version control using Git and GitHub.

The application provides a foundation for further improvements, including:

- User authentication and registration.
- Blog search and pagination.
- Improved form validation and email notifications.
- Deployment to a production hosting environment.
- Integration with additional database and cloud services.

Overall, this project has helped me develop practical web development skills and gain confidence in building database-driven applications with Django.