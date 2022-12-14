"""QuizApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from Quiz import views

urlpatterns = [
    path('', views.dashboard_view, name="dashboard"),
    path('new_quiz/', views.new_quiz_view, name="new_quiz"),
    path('quiz/<int:quiz_id>/<int:question_no>', views.question_view, name="question"),
    path('quiz/<int:quiz_id>/add_question/<int:question_no>', views.add_question_view, name="add_question"),
    path('results/<int:quiz_id>', views.result_view, name="results"),
    path('delete/<int:quiz_id>', views.delete_quiz_view, name="delete_quiz"),
    path('logout', views.signout_view, name="signout"),
]
