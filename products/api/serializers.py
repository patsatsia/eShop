from rest_framework import serializers
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id", "name", "category", "description", "price", 
            "quantity", "created_at", "created_by", "updated_at", 
            "updated_by", "deleted_at", "deleted_by",
        )