
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage, NewsletterSubscription


def home(request):
    return render(request, 'website/index.html')


def blog(request):
    return render(request, 'website/blog.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        messages.success(request, 'Your message has been sent successfully!')

    return redirect('/#contact')  # Redirect back to the contact section of the home page

def newsletter(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        if email:
            NewsletterSubscription.objects.get_or_create(
                email=email
            )

            messages.success(
                request,
                'You have successfully subscribed to our newsletter!'
            )

    return redirect('/#subscribe')  # Redirect back to the newsletter section of the home page