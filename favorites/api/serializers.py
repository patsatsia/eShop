from rest_framework import serializers
from favorites.models import FavProduct
from products.models import Product
from django.contrib.auth.models import User

class FavProductSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    item = serializers.StringRelatedField()
    item_id = serializers.PrimaryKeyRelatedField(source='item', queryset=Product.objects.all(), write_only=True)
    user_id = serializers.PrimaryKeyRelatedField(source='user', queryset=User.objects.all(), write_only=True)

    class Meta:
        model = FavProduct
        fields = ("id", "user", "item", "item_id", "user_id")