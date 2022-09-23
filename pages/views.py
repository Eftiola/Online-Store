from django.shortcuts import render,redirect
from .forms import FeedbackForm
from django.http import HttpResponseRedirect
from django.contrib import messages


def home(request):
    return render(request, "home.html")


def contact_us(request):
    form = FeedbackForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "We have recevied your feedback")
        return redirect("contact-us")
    return render(request, "contact_us.html", {"form": form})
