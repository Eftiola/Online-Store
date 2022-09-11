
from django.shortcuts import render, redirect, reverse, get_object_or_404
from categories.models import Category
from .models import Product
from django.core.paginator import Paginator



def get_products(request):
   
    categories = Category.objects.all()
    products = Product.objects.all()

    try:
        page_no = int(request.GET.get("page", "1"))
    except ValueError:
        page_no = 1

    paginator = Paginator(products, per_page=4)
    page_obj = paginator.page(page_no)

    return render( request,"product_list.html",
        context={"categories": categories, "page_obj": page_obj},
    )

def get_product_details(request, pk):
    product = get_object_or_404(Product,pk=pk)
    return render(request,"product_details.html",context={"product": product})