from django.contrib import admin
from django.urls import path
from .views import *
app_name="article"

urlpatterns = [
   path('dashboard/',DashboardView.as_view(),name="dashboard"),
   path('addarticle/',AddArticleView.as_view(),name="addarticle"),
   path('article/<int:id>',DetailView.as_view(),name="detail"),
   path('update/<int:id>',UpdateArticleView.as_view(),name="update"),
   path('delete/<int:id>',DeleteArticleView.as_view(),name="delete"),
   path('comment/<int:id>',AddCommentView.as_view(),name="comment"),
   path('vote/<int:id>',FeedBackView.as_view(),name="feedback"),
   path('',ArticlesView.as_view(),name="articles"),
]