from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50,label="Username")
    password = forms.CharField(label="Password",widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, label = "Username")
    password = forms.CharField(max_length=20,label="Password",widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=20,label="Confirm Password",widget=forms.PasswordInput)
    
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError('This username is being used...')

        if password and confirm and password != confirm :
            raise forms.ValidationError("Passwords are not matching")
        
        values = {
            "username": username,
            "password": password,

        }
        return values