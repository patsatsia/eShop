from rest_framework import serializers
from products.models import Product
from category.models import Category
from category.api.serializers import CategorySerializer
from django.contrib.auth.models import User
from dj_rest_auth.serializers import LoginSerializer, UserDetailsSerializer

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
        validated_data.pop("category")
        category_ids = self.context.get('request').data.get('category_ids')
        product = Product.objects.create(**validated_data)
        for item in category_ids:
            category = Category.objects.get(id=item)
            product.category.add(category)
        return product

    
    def update(self, instance, validated_data):
        instance.name = validated_data["name"]
        instance.price = validated_data["price"]
        instance.description = validated_data["description"]
        instance.quantity = validated_data["quantity"]

        instance.updated_by = self.context['request'].user #????????

        category_ids = self.context.get('request').data.get('category_ids')
        instance.category.set(category_ids)

        # instance.category.clear()
        # for item in category_ids:
        #     category = Category.objects.get(id=item)
        #     instance.category.add(item)        
        instance.save()
        
        return instance