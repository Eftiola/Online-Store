from django.forms import ModelForm
from .models import  Product

from django.contrib.auth import get_user_model

User = get_user_model()

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = [
            'name', 'description','slug', 'image', 'category', 'price','product_type'
        ]