from django import forms
from django.contrib.auth import  authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import User
class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "first_name","role","email","country","street_address" ]
        