from django.forms import ModelForm
from .models import  Product

from django.contrib.auth import get_user_model

User = get_user_model()

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = [
            'title', 'description','slug', 'photo', 'category', 'price','product_type'
        ]