from products.api.serializers import ProductSerializer
from rest_framework import views, viewsets
from products.models import Product

from rest_framework import permissions
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated

class ProductView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = (AllowAny, )
        else:
            self.permission_classes = (IsAdminUser, )

        return super(ProductView, self).get_permissions()

