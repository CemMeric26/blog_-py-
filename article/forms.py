from django import forms
from .models import Article,Video

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields= ["title","content","article_image"]

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ["title","url","video_id"]

"""class TakenCourseForm(forms.ModelForm):
    class Meta:
        model = TakenCourse
        fields = ["title","content","article_image"]

"""