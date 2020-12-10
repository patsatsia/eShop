from products.api.serializers import ProductSerializer
from rest_framework import views, viewsets
from products.models import Product
from django.utils import timezone

from rest_framework import permissions
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated

class ProductView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by = self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by = self.request.user)

    def perform_destroy(self, instance):
        instance.deleted_by = self.request.user 
        instance.deleted_at = timezone.now()
        instance.save()






