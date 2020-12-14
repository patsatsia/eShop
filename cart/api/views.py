from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet

from cart.models import CartItem
from cart.api.serializers import CartItemSerializer

class CartItemView(viewsets.ModelViewSet):
    serializer_class = CartItemSerializer
    queryset = CartItem.objects.all()