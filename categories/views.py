from django.shortcuts import render, redirect, reverse, get_object_or_404



def get_categories(request):
  return render(request, 'categories_list.html')
