from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.home, name='home'),
    path('Privacy/',views.privacypolicy,name='privacypolicy'),
    path('Terms/', views.termsagreement,name='termsagreement'),
    path('FAQs/', views.FAQs,name='FAQs'),
    path('ContactUs/', views.contact,name='contact'),
    path('register/', views.register, name='register'),
    path('login/', auth_view.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    path('home/', views.profile, name='profile'),

]
