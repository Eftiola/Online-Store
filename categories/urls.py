from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_categories_list, name="categories_list"),
    path("add/", views.category_add, name="category_add"),
]
