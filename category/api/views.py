from .serializers import CategorySerializer
from category.models import Category

from rest_framework import status, serializers
from rest_framework.response import Response
from rest_framework import views, viewsets
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

class CategoryView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(deleted_by = None)

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = (AllowAny, )
        else:
            self.permission_classes = (IsAdminUser, )

        return super(CategoryView, self).get_permissions()

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)
    

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        deleter = self.request.user
        self.perform_destroy(instance, deleter)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance, deleter):
        instance.soft_delete(deleter)