from django.shortcuts import render
from .forms import FeedbackForm
from django.http import HttpResponseRedirect
from django.contrib import messages


def contact_us(request):
    form = FeedbackForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "We have recevied your feedback")
        return HttpResponseRedirect("")
    return render(request, "contact_us.html", {"form": form})
