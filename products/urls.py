from django.urls import path

from . import views
 

# app_name = "products"

urlpatterns = [
    path("", views.get_products, name="product_list"), 
    path("<int:pk>/", views.get_product_details, name="product_details"),
    
    
]
