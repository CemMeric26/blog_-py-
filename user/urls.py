from django.contrib import admin
from django.urls import path
from .views import *

app_name="user"

urlpatterns = [
   path('signup/',SignUpView.as_view(),name="signup"),
   path('signup/student/',StudentSignUpView.as_view(),name="student_signup"),
   path('signup/teacher',TeacherSignUpView.as_view(),name="teacher_signup"),
   path('login/',Login2View.as_view(),name="login"),
   path('logout/',Logout2View.as_view(),name="logout"),
   path('loginins/',LoginInsView.as_view(),name="loginins"),
   path('loginstu/',LoginStuView.as_view(),name="loginstu"),
]
"""path('register/',RegisterView.as_view(),name="register"),
path('login/',LoginUserView.as_view(),name="login"),
path('logout/',LogoutUserView.as_view(),name="logout"),"""