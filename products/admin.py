from django.contrib import admin
from .models import Product,OrderLine, Order

admin.site.register(Product),
admin.site.register(OrderLine),
admin.site.register(Order)

