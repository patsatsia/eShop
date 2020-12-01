from django.db import models
from category.models import Category

class Product(models.Model):
    category = models.ManyToManyField(Category, blank=False)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField(default=0)

    class Meta:
        ordering = ("name", )

    def __str__(self):
        return self.name