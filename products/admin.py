from django.contrib import admin
from .models import Product,OrderLine, Order


admin.site.register(OrderLine),
admin.site.register(Order)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title',  'category', 'price','product_type']
    list_filter = ['title']
    


admin.site.register(Product, ProductAdmin)