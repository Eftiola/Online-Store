from django.db import models


class Category(models.Model):
    parent = models.ForeignKey(
        "self", related_name="children", on_delete=models.CASCADE, blank=True, null=True
    )
    name = models.CharField(max_length=30, null=False, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    # is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/%s/" % (self.slug)

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name)
    #     return super().save(*args, **kwargs)
