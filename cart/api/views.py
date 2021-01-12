from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from cart.models import CartItem, Cart
from cart.api.serializers import CartItemSerializer, CartSerializer, AddToCartSerializer

class CartView(viewsets.ModelViewSet):
    serializer_class = CartItemSerializer
    #queryset = Cart.objects.get(owner=self.request.user)

    def list(self, request, *args, **kwargs):
        cart, created = Cart.objects.get_or_create(owner=request.user)
        serializer = CartSerializer(cart, context={'request': request})
        return Response(serializer.data)


    def get_queryset(self):
        current = self.request.user
        return Cart.objects.filter(owner=current)

    def get_serializer_class(self):
        if self.action == "create":
            return AddToCartSerializer
        return CartItemSerializer
    




        
            
