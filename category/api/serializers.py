from category.models import Category
from rest_framework import serializers
from rest_framework.serializers import SerializerMetaclass

class CategorySerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Category
        fields = "__all__"