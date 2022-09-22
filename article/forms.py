from django import forms
from .models import Article,Video

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields= ["title","content","article_image"]

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ["title","url"]

"""class TakenCourseForm(forms.ModelForm):
    class Meta:
        model = TakenCourse
        fields = ["title","content","article_image"]

"""