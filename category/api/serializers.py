from category.models import Category
from rest_framework import serializers
from rest_framework.serializers import SerializerMetaclass

class CategorySerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Category
        fields = ("id", "name", "created_at", "created_by", "updated_at", "updated_by", "deleted_at", "deleted_by",)
        # depth = 1

        #fields = ("id", "name", "created_by", "updated_by", "deleted_by",)