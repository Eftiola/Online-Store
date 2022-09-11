
from django.shortcuts import render, redirect, reverse, get_object_or_404



def get_products(request):
    return render(request, "product_list.html")