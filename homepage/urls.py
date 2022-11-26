from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    
    path('login.html', views.login, name='login'),
    path('Policy.html', views.policy, name='Policy'),
    path('terms.html', views.terms, name='terms'),
    path('contact.html', views.contact, name='contact'),

    path('', views.index, name='index')
]