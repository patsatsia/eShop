from .serializers import CategorySerializer
from category.models import Category
from django.utils import timezone

from rest_framework import status, serializers
from rest_framework.response import Response
from rest_framework import views, viewsets
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

class CategoryView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(deleted_by = None)
    #permission_classes = (IsAdminUser, )

    def perform_create(self, serializer):
        serializer.save(created_by = self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

    def perform_destroy(self, instance):
        instance.deleted_by = self.request.user 
        instance.deleted_at = timezone.now()
        instance.save()