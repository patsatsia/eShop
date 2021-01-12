from django.db import models
from category.models import Category
from django.contrib.auth.models import User

class Product(models.Model):
    category = models.ManyToManyField(Category, blank=False)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add = True, null = True)
    created_by = models.ForeignKey(User, default = None, blank=True, null=True, on_delete=models.DO_NOTHING, related_name="products_created_by")
    updated_at = models.DateTimeField(auto_now = True, null = True)
    updated_by = models.ForeignKey(User, default = None, blank=True, null=True, on_delete=models.DO_NOTHING, related_name="products_updated_by")
    deleted_at = models.DateTimeField(null = True)
    deleted_by = models.ForeignKey(User, default = None, blank=True, null=True, on_delete=models.DO_NOTHING, related_name='products_deleted_by')

    class Meta:
        ordering = ("name", )

    def __str__(self):
        return self.name