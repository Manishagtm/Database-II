from django.contrib import admin
from django import forms
from myapp.models import Login, Sign
from myapp.forms import LoginForm, SignForm

# Register your models here.
admin.site.register(Login)
admin.site.register(Sign)


class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = ["email", "password"]