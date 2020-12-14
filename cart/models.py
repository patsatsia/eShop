from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Cart(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    number_of_items = models.PositiveIntegerField(default=0)
    total = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)


    def __str__(self):
        return "User: {}, items in cart: {}".format(self.owner, self.number_of_items)



class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.id
