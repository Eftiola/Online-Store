
from django.shortcuts import render, redirect

from .models import Category

from .forms import CategoryForm


def get_categories_list(request):
    cat_list = Category.objects.all()
    return render(request, "categories_list.html", context={"cat_list": cat_list})


def category_add(request):
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            return redirect("categories_list")
    else:
        form = CategoryForm()
    return render(request, "add_categories.html", context={"form": form})
