from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Login, Sign


class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = ["email", "password"]


class SignForm(forms.ModelForm):
    class Meta:
        model = Sign
        fields = ('Name', 'Email', 'Password', 'password1')

