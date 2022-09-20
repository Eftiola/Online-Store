from django.contrib import admin
from .models import Product


# admin.site.register(OrderLine),
# admin.site.register(Order)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name',  'category', 'price','product_type']
    list_filter = ['name']
    


admin.site.register(Product, ProductAdmin)