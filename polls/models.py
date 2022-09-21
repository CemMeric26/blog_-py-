from django.db import models
from article.models import Article
# Create your models here.

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
