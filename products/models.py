from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from categories.models import Category

# Create your models here.

LABEL_CHOICES = (
    ("P", "primary"),
    ("S", "secondary"),
)


class Product(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100)

    description = models.TextField(null=True)
    # thumbnail=models.URLField()
    slug = models.SlugField(null=True, blank=True, unique=True)
    photo = models.ImageField(null=True, blank=True, upload_to="products")
    category = models.ForeignKey(
        Category, null=True, blank=True, on_delete=models.SET_NULL
    )
    price = models.FloatField()
    product_type = models.CharField(choices=LABEL_CHOICES, max_length=1)

    def __str__(self):
        return self.title


class OrderLine(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    product_price=models.FloatField()
    ordered = models.BooleanField(default=False)

  

    def __str__(self):
        return f"{self.quantity} of {self.product.title}"
    
    def get_total_product_price(self):
        return self.quantity * self.product.price
