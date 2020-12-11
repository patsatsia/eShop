from category.models import Category
from rest_framework import serializers
from rest_framework.serializers import SerializerMetaclass
from dj_rest_auth.serializers import UserDetailsSerializer

class CategorySerializer(serializers.ModelSerializer):
    created_by = UserDetailsSerializer(required=False)
    updated_by = UserDetailsSerializer(required=False)
    deleted_by = UserDetailsSerializer(required=False)

   
    class Meta:
        model = Category
        fields = ("id", "name", "created_at", "created_by", "updated_at", "updated_by", "deleted_at", "deleted_by",)