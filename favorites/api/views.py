from favorites.models import FavProduct
from favorites.api.serializers import FavProductSerializer

from rest_framework import viewsets, permissions
from rest_framework.viewsets import ModelViewSet


class FavProductView(viewsets.ModelViewSet):
    serializer_class = FavProductSerializer
    #queryset = FavProduct.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


    def get_queryset(self):
        current = self.request.user
        return FavProduct.objects.filter(user=current)

    # def get_queryset(self):
    #     user = self.request.user
    #     queryset = self.queryset.filter(owner=user)
    #     return queryset    CHECK IF IT WORKS