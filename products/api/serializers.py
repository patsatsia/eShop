from rest_framework import serializers
from products.models import Product
from category.models import Category
from category.api.serializers import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)


    created_by = serializers.StringRelatedField()
    updated_by = serializers.StringRelatedField()
    deleted_by = serializers.StringRelatedField()
    

    class Meta:
        model = Product
        fields = (
            "id", "name", "category", "description", "price", 
            "quantity", "created_at", "created_by", "updated_at", 
            "updated_by", "deleted_at", "deleted_by",
        )

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        product = Product.objects.create(**validated_data)
        for category in category_data:
            category, created = Category.objects.get_or_create(name=category["name"])
            product.category.add(category)
            #Category.objects.create(product=product, **category )
        return product

    # def create(self, validated_data):
    #     category = validated_data.pop('category')
    #     product = Product.objects.create(**validated_data)
    #     Category.objects.create(product=product, **item)

    #     return product
