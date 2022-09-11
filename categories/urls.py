from django.urls import path

from . import views
 

# app_name = "categories"

urlpatterns = [
    path("", views.get_categories, name="categories_list"), 
]
