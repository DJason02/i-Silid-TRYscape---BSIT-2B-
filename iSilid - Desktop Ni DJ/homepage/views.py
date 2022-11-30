from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {})


def login(request):
    return render(request, 'login.html', {})


def policy(request):
    return render(request, 'Policy.html', {})


def terms(request):
    return render(request, 'terms.html', {})


def contact(request):
    return render(request, 'contact.html', {})

def signup(request):
    return render(request, 'signup.html', {})

