from importlib.resources import contents
from django.db import models
from ckeditor.fields import RichTextField
from django.core.validators import MaxValueValidator, MinValueValidator
#from user.models import User
# Create your models here.

class Article(models.Model):
    author = models.ForeignKey("user.User",on_delete=models.CASCADE,verbose_name="Author")
    title = models.CharField(max_length=50)
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True)
    article_image = models.FileField(blank=True,null=True,verbose_name="Add image to the article")
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_date']

class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name="Article",related_name="comments")
    comment_author = models.CharField(max_length=50,verbose_name="Name")
    comment_content = models.CharField(max_length=200,verbose_name="comment")
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.comment_content

    class Meta:
        ordering = ['-comment_date']

class TakenCourse(models.Model):
    student = models.ForeignKey("user.Student", on_delete=models.CASCADE, related_name='taken_courses')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='taken_courses')
    score = models.IntegerField(default=0,
                                validators=[
                                    MaxValueValidator(5),
                                    MinValueValidator(0),
                                ]
    )   #rating for the taken course

    def __str__(self):
        return self.article.title
