from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    email = models.TextField()
    password = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Quizzes(models.Model):
    answer = models.CharField(max_length=100)
    questions = models.TextField()


class ToDoList(models.Model):
    tasks = models.TextField()


class Notes(models.Model):
    word = models.CharField(max_length=50)
    descriptions = models.TextField()

