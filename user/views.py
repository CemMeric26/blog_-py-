import imp
from multiprocessing import context
from django.shortcuts import render,redirect
#from .forms import RegisterForm,LoginForm

#from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.views import View
from django.views.generic import CreateView
from .models import User
from .forms import TeacherSignUpForm,StudentSignUpForm,LoginForm
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.


class SignUpView(View):
    def get(self,request):
        return render(request,"signup.html")

class TeacherSignUpView(View):
    model = User
    def get(self,request,**kwargs):
        form = TeacherSignUpForm(None)
        kwargs['user_type'] = 'teacher'
        context = {
            "form": form
        }
        return render(request, "signup_form.html", context)


    def post(self,request):
        form = TeacherSignUpForm(request.POST or None)
        if form.is_valid():
            user = form.save()
           #left in hereee
            login(self.request,user)  # this function handles with login process
            messages.success(request, "Registered succesfully")
            return redirect("index")  # goes to main page after succesfull login
        context = {
            "form": form
        }
        return render(request, "signup_form.html", context)



class StudentSignUpView(View):
    model = User
    def get(self,request, **kwargs):
        form = StudentSignUpForm(None)
        context = {
            "form":form
        }
        kwargs['user_type'] = 'student'
        return render(request, "signup_form.html", context)

    def post(self, request):
        form = StudentSignUpForm(request.POST or None)
        if form.is_valid():
            user = form.save()

            login(request, user)  # this function handles with login process
            messages.success(request, "Registered successfully")
            return redirect("index")  # goes to main page after succesfull login
        context = {
            "form": form
        }
        return render(request, "signup_form.html", context)

class Login2View(View):
    def get(self,request):
        form = LoginForm(None)

        context = {
            "form": form
        }

        return render(request, "login.html",context)
    def post(self,request):
        form = LoginForm(request.POST or None)

        context = {
            "form": form
        }

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            print(user)
            if user is None:
                messages.info(request, "Username or password is wrong")
                return render(request, "login.html", context)

            messages.success(request, "Login successfully")
            login(request, user)
            return redirect("index")

        return render(request, "login.html", context)

class LoginInsView(View):
    def get(self,request):
        form = LoginForm(None)

        context = {
            "form": form
        }

        return render(request, "loginins.html",context)
    def post(self,request):
        form = LoginForm(request.POST or None)

        context = {
            "form": form
        }

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)

            if user is None:
                messages.info(request, "Username or password is wrong")
                return render(request, "login.html", context)

            messages.success(request, "Login successfully")
            login(request, user)
            return redirect("index")

        return render(request, "loginins.html", context)

class LoginStuView(View):
    def get(self,request):
        form = LoginForm(None)

        context = {
            "form": form
        }

        return render(request, "loginstu.html",context)
    def post(self,request):
        form = LoginForm(request.POST or None)

        context = {
            "form": form
        }

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)

            if user is None:
                messages.info(request, "Username or password is wrong")
                return render(request, "login.html", context)

            messages.success(request, "Login successfully")
            login(request, user)
            return redirect("index")

        return render(request, "loginstu.html", context)

class Logout2View(View):
    def get(self,request):
        logout(request)
        messages.success(request, "Logout successfully")
        return render(request,"index.html")

