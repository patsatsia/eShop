from .serializers import CategorySerializer
from category.models import Category

from rest_framework import views, viewsets
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

class CategorySerializerView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = (AllowAny, )
        else:
            self.permission_classes = (IsAdminUser, )

        return super(CategorySerializerView, self).get_permissions()