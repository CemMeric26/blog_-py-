from django import forms
from .models import Article,TakenCourse

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields= ["title","content","article_image"]

"""class TakenCourseForm(forms.ModelForm):
    class Meta:
        model = TakenCourse
        fields = ["title","content","article_image"]

"""