from django.contrib.auth.models import AbstractUser
from django.db import models
from article.models import Article

from django.utils.html import escape, mark_safe


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='student')
    courses = models.ManyToManyField(Article,
                                     through="article.TakenCourse")  # you need to implement through="takencourse"

    def __str__(self):
        return self.user.username
