from django.shortcuts import render, redirect, get_object_or_404
from categories.models import Category
from .models import Product, OrderLine, Order
from django.core.paginator import Paginator
from .forms import ProductForm
from django.utils import timezone


def get_products(request):
    page_no = int(request.GET.get("page", "1"))
    page_size = int(request.GET.get("size", "3"))

    products = Product.objects.order_by("-id").all()
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
        prod = Product.objects.filter(title__contains=searched)
        cats = Category.objects.filter(name__contains=searched)
        return render(
            request,
            "search_product.html",
            {"searched": searched, "prod": prod, "cats": cats},
        )

    else:

        return render(request, "search_product.html", {})


def get_product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "product_details.html", context={"product": product})


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


def add_to_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)
    order_line, created = OrderLine.objects.get_or_create(
        product=product, user=request.user, ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order product is in the order
        if order.products.filter(product__slug=product.slug).exists():
            order_line.quantity += 1
            order_line.save()
            # messages.info(request, "This product quantity was updated.")
            # return redirect("core:order-summary")
        else:
            order.products.add(order_line)
            # messages.info(request, "This product was added to your cart.")
            # return redirect("core:order-summary")
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.products.add(order_line)
        # messages.info(request, "This product was added to your cart.")
    return redirect("product_list")
