from django.db import models

from django.conf import settings
from categories.models import Category

# Create your models here.

LABEL_CHOICES = (
    ("P", "primary"),
    ("S", "secondary"),
)


class Product(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)

    description = models.TextField(null=True)
    # thumbnail=models.URLField()
    slug = models.SlugField(null=True, blank=True, unique=True)
    image = models.ImageField(null=True, blank=True, upload_to="products")
    category = models.ForeignKey(
        Category, null=True, blank=True, on_delete=models.SET_NULL
    )
    price = models.FloatField()
    product_type = models.CharField(choices=LABEL_CHOICES, max_length=1)

    def __str__(self):
        return self.name
