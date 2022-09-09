from django.urls import path

from . import views

app_name='polls'
urlpatterns = [
    path('', views.feedback, name='feedback'),
    path('success/', views.success, name='success'),

]
