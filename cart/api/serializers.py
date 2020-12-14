from rest_framework import serializers
from cart.models import CartItem
from dj_rest_auth.serializers import UserDetailsSerializer

class CartItemSerializer(serializers.ModelSerializer):
    user = UserDetailsSerializer()

    class Meta:
        model = CartItem
        fields = "__all__"