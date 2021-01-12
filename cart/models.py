from django.db import models
from django.contrib.auth.models import User
from products.models import Product        


class Cart(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    cart_items = models.ManyToManyField('CartItem', related_name='cart_item', blank=True)
    # number_of_items = models.PositiveIntegerField(default=0, null=True)
    # total = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)


    def __str__(self):
        return "User: {}, items in cart: {}".format(self.owner, self.number_of_items)
    
    @property
    def total_price(self):
        total_price = 0
        for item in self.cart_items.all():
            total_price += item.total_price
        return total_price

    @property
    def number_of_items(self):
        num = 0
        for item in self.cart_items.all():
            num += item.quantity
        return num


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, default=None, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    @property
    def total_price(self):
        return (self.product.price * self.quantity)