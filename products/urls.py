from django.urls import path

from . import views
 

# app_name = "products"

urlpatterns = [
    path("", views.get_products, name="product_list"), 
    path("<int:pk>/", views.get_product_details, name="product_details"),
     path("add/", views.product_add, name="product_add"),
    path("product/<int:pk>/", views.edit_product, name='product-edit'),
    
    
]
