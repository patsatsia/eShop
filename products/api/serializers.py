from rest_framework import serializers
from products.models import Product
from category.models import Category
from category.api.serializers import CategorySerializer
from django.contrib.auth.models import User
from dj_rest_auth.serializers import UserDetailsSerializer

class ProductSerializer(serializers.ModelSerializer):
    category     = CategorySerializer(many=True, required=False, read_only=True)  
    category_ids = serializers.PrimaryKeyRelatedField(source='category', many=True, queryset=Category.objects.all())
    created_by   = UserDetailsSerializer(required=False)
    updated_by   = UserDetailsSerializer(required=False)
    deleted_by   = UserDetailsSerializer(required=False)

    class Meta:
        model = Product
        fields = (
            "id", "name", "category_ids", "category", "description", "price", 
            "quantity", "created_at", "created_by", "updated_at", 
            "updated_by", "deleted_at", "deleted_by",
        )
        # depth = 1

    def create(self, validated_data):
        categories = validated_data.pop("category")
        product = super().create(validated_data)
        for item in categories:
            product.category.add(item)
        return product

    
    def update(self, instance, validated_data):
        categories = validated_data.pop("category")
        instance = super().update(instance, validated_data)
        instance.category.set(categories)
        instance.save()
        return instance