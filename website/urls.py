from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog.html', views.blog, name='blog'),
    path('contact.html', views.contact, name='contact'),
    path('newsletter/', views.newsletter, name='newsletter'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
]