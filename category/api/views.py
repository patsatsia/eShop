from .serializers import CategorySerializer
from category.models import Category

from rest_framework import status
from rest_framework.response import Response
from rest_framework import views, viewsets
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

class CategoryView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(delete=False)

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = (AllowAny, )
        else:
            self.permission_classes = (IsAdminUser, )

        return super(CategoryView, self).get_permissions()


    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        updater = self.request.user
        serializer.save()
        instance.get_updater(updater)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
    

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        deleter = self.request.user
        self.perform_destroy(instance, deleter)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance, deleter):
        instance.soft_delete(deleter)