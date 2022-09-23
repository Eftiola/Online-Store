from django.shortcuts import render, redirect, get_object_or_404
from categories.models import Category
from .models import Product
from django.core.paginator import Paginator
from .forms import ProductForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.utils import timezone

# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.conf import settings

# import stripe
# from django.contrib.auth.models import Group, User, Permission
from django.contrib.auth.decorators import login_required, permission_required

from .models import Product
from .cart import Cart


def get_products(request):
    page_no = int(request.GET.get("page", "1"))
    page_size = int(request.GET.get("size", "3"))

    products = Product.objects.order_by("-id").all()

    category_id = request.GET.get("cat")
    if category_id is not None:
        try:
            category = Category.objects.get(pk=category_id)
        except Category.DoesNotExist:
            pass
        else:
            categories = category.get_descendants(include_self=True)
            products = products.filter(category__in=categories)

    paginator = Paginator(products, page_size)
    page_obj = paginator.page(page_no)

    return render(
        request,
        "product_list.html",
        context={"products": products, "paginator": paginator, "page_obj": page_obj},
    )


def search_product(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        prod = Product.objects.filter(name__contains=searched)
        cats = Category.objects.filter(name__contains=searched)
        return render(
            request,
            "search_product.html",
            {"searched": searched, "prod": prod, "cats": cats},
        )

    else:

        return render(request, "search_product.html", {})


@login_required
def get_product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "product_details.html", context={"product": product})


@permission_required("product.add_product", login_url="/login", raise_exception=True)
def product_add(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect("product_list")
    else:
        form = ProductForm()
    return render(request, "product_add.html", context={"form": form})


def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save()
            return redirect("product_list")
    else:
        form = ProductForm(instance=product)
    return render(
        request,
        "product_add.html",
        context={
            "form": form,
            "product": product,
        },
    )


@login_required
def get_product_list(request):
    products = Product.objects.all()
    return render(request, "shop/product_list.html", context={"products": products})


@login_required
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("product_list")


@login_required
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required
def cart_detail(request):
    return render(request, "cart_detail.html")
