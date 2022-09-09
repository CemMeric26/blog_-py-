import datetime
from django.db import models
from django.contrib import admin
from django.utils import timezone
from article.models import Article


class Poll(models.Model):
    CHOICES = (
        ('Strongly Disagree', 'Strongly Disagree'),
        ('Disagree', 'Disagree'),
        ('Sometimes', 'Sometimes'),
        ('Agree', 'Agree'),
        ('Strongly Agree', 'Strongly Agree'),
    )
    sub_date = models.DateTimeField(auto_now=True)

    article_name = models.ForeignKey(Article,verbose_name="course name",on_delete=models.CASCADE)

    organization = models.CharField(verbose_name="Course organizaiton was?",max_length=225,choices=CHOICES)
    contribution = models.CharField(verbose_name="The instructor's contribution to the course was?",max_length=225,choices=CHOICES)
    course_content = models.CharField(verbose_name="The course content was?",max_length=225,choices=CHOICES)
    general = models.CharField(verbose_name="The course as awhole was?",max_length=225,choices=CHOICES)
    feedback = models.TextField(verbose_name="Any other feedback",blank=True)

    class Meta:
        verbose_name = 'Poll'

    def __str__(self):
        return self.article_name.title

# Create your models here.
""""
class Question(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name="Article",related_name="question")
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text
    class Meta:
        ordering=['-pub_date']
    """
"""
        @admin.display(
            boolean=True,
            ordering='pub_date',
            description='Published recently?',
        )
        def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    """
"""

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

"""