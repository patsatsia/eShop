from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class FavProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favorite")
    item = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="fav_item", null=True)

    def __str__(self):
        return "User: {}, Favorite Product: {}".format(self.user, self.item)