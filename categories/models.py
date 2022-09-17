from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    parent = TreeForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )
    name = models.CharField(max_length=30, null=False, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    # is_active = models.BooleanField(default=True)

    class MPTTMeta:
        order_insertion_by = ["name"]
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/%s/" % (self.slug)

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name)
    #     return super().save(*args, **kwargs)
