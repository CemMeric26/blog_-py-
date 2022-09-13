from importlib.resources import contents
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Author")
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


class Poll(models.Model):
    CHOICES = (
        ('Strongly Disagree', 'Strongly Disagree'),
        ('Disagree', 'Disagree'),
        ('Sometimes', 'Sometimes'),
        ('Agree', 'Agree'),
        ('Strongly Agree', 'Strongly Agree'),
    )
    sub_date = models.DateTimeField(auto_now=True)

    article_name = models.ForeignKey(Article,verbose_name="course name",on_delete=models.CASCADE,related_name="poll")

    organization = models.CharField(verbose_name="Course organizaiton was?",max_length=225,choices=CHOICES)
    contribution = models.CharField(verbose_name="The instructor's contribution to the course was?",max_length=225,choices=CHOICES)
    course_content = models.CharField(verbose_name="The course content was?",max_length=225,choices=CHOICES)
    general = models.CharField(verbose_name="The course as awhole was?",max_length=225,choices=CHOICES)
    feedback = models.TextField(verbose_name="Any other feedback",blank=True)

    class Meta:
        verbose_name = 'Poll'

    def __str__(self):
        return self.article_name.title
