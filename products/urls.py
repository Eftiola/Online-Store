from django.urls import path

from . import views
 

# app_name = "products"

urlpatterns = [
    path("", views.get_products, name="product_list"), 
    
]
