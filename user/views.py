import imp
from multiprocessing import context
from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm

from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.views import View
# Create your views here.


class RegisterView(View):
    def get(self,request):
        form = RegisterForm(None)
        context = {
            "form": form
        }
        return render(request, "register.html", context)
    def post(self,request):
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            newUser = User(username=username)
            newUser.set_password(password)
            newUser.save()  # saving to data
            login(request, newUser)  # this function handles with login process
            messages.success(request, "Registered succesfully")
            return redirect("index")  # goes to main page after succesfull login
        context = {
            "form": form
        }
        return render(request, "register.html", context)

"""def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username = username)
        newUser.set_password(password)

        newUser.save() # saving to data

        login(request,newUser) #this function handles with login process

        messages.success(request,"Registered succesfully")
        
        return redirect("index") #goes to main page after succesfull login
        
    
    context = {
        "form" : form
        }    
    return render(request,"register.html",context)
"""


class LoginUserView(View):
    def get(self,request):
        form = LoginForm(None)

        context = {
            "form": form
        }

        return render(request, "login.html", context)
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

            messages.success(request, "Login succesfully")
            login(request, user)
            return redirect("index")

        return render(request, "login.html", context)

"""def loginUser(request):
    form = LoginForm(request.POST or None)

    context = {
        "form": form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")


        user = authenticate(username=username, password=password)

        if user is None:
            messages.info(request,"Username or password is wrong")
            return render(request,"login.html",context)

        messages.success(request,"Login succesfully")
        login(request,user)
        return redirect("index")

    return render(request,"login.html",context)
"""

class LogoutUserView(View):
    def get(self,request):
        logout(request)
        messages.success(request, "Logout successfully")

        return redirect("index")

"""def logoutUser(request):
    logout(request)
    messages.success(request,"Logout successfully")

    return redirect("index")
"""