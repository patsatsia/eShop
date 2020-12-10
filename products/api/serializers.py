from rest_framework import serializers
from products.models import Product
from category.models import Category
from category.api.serializers import CategorySerializer
from django.contrib.auth.models import User
from dj_rest_auth.serializers import LoginSerializer, UserDetailsSerializer


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True, required=False)  
    category_ids = serializers.PrimaryKeyRelatedField(source='category', many=True, queryset=Category.objects.all())
    created_by = UserDetailsSerializer(required=False)
    updated_by = UserDetailsSerializer(read_only=True)
    deleted_by = UserDetailsSerializer(read_only=True)

    class Meta:
        model = Product
        fields = (
            "id", "name", "category_ids", "category", "description", "price", 
            "quantity", "created_at", "created_by", "updated_at", 
            "updated_by", "deleted_at", "deleted_by",
        )
        # depth = 1

    def create(self, validated_data):
        validated_data.pop("category", [])
        product = Product.objects.create(**validated_data)
        category = Category.objects.get(pk = category_ids)
        product.category.adsetd(category)
        return product
