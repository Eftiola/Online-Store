from django.db import models


class Feedback(models.Model):
    title = models.CharField(max_length=30)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField()
    order_number = models.IntegerField()
    feedback = models.TextField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title
