from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib.auth import login, logout
from .forms import UserCreateForm


def sign_up(request):
    if request.method == "POST":
        form = UserCreateForm(request.POST)
        if form.is_valid():
           user= form.save()
           login(request, user)
           return redirect("home")
    else:
        form = UserCreateForm()
    return render(request, "sign_up.html", {"form": form})
