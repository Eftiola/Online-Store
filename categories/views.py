from django.shortcuts import render, redirect


from .models import Category
from .forms import CategoryForm


# from mptt.exceptions import InvalidMove
# from mptt.forms import MoveNodeForm


def get_categories_list(request):
    categories = Category.objects.all()

    return render(
        request,
        "categories_list.html",
        context={"categories": categories},
    )


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
