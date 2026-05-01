from django.shortcuts import render, redirect
from .models import Project
from .forms import ContactForm
from django.core.mail import send_mail
from django.contrib import messages


def home(request):
    projects = Project.objects.all()[:3]
    return render(request, 'core/home.html', {'projects': projects})


def about(request):
    return render(request, 'core/about.html')


def projects(request):
    projects = Project.objects.all()
    return render(request, 'core/projects.html', {'projects': projects})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f"Portfolio Message from {form.cleaned_data['name']}",
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['your_email@gmail.com'],
                fail_silently=False,
            )
            messages.success(request, "Message sent successfully!")
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'core/contact.html', {'form': form})