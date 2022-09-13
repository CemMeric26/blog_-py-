from django import forms
from .models import Article,Poll

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields= ["title","content","article_image"]
class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields= ["organization","contribution","course_content","general","feedback"]
