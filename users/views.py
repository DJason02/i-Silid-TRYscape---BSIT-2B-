from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Contact
from django.core.mail import message
from django.core.mail.message import EmailMessage
from django.conf import settings
from django.core.mail import send_mail
from django.core import mail
from django.contrib.auth.models import User
from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    return render(request,'users/index.html')

def privacypolicy(request):
    return render(request,'users/policy.html')

def termsagreement(request):
    return render(request,'users/terms.html')

def contact(request):
	if request.method == 'POST':
		message = request.POST['Subject']
		send_mail('Contact Form',message, 
		settings.EMAIL_HOST_USER,
		['isilid2b@outlook.com'], 
		fail_silently=False)
	return render(request, 'users/contact.html')


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})


@login_required()
def profile(request):
    return render(request, 'users/profile.html')


