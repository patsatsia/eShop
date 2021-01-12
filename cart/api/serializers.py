from rest_framework import serializers
from cart.models import CartItem, Cart
from dj_rest_auth.serializers import UserDetailsSerializer
from products.api.serializers import ProductSerializer




class CartItemSerializer(serializers.ModelSerializer):
    #cart = CartSerializer(required=True)
    product = serializers.StringRelatedField(read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = "__all__"

    def get_total_price(self, object):
        return object.total_price


class AddToCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ('product', 'quantity' )

    def create(self, validated_data):
        user = self.context.get('request').user
        product = validated_data.get('product')
        quantity = validated_data.get('quantity')
        cart, created = Cart.objects.get_or_create(owner=user)
        cart_item = CartItem.objects.filter(cart=cart, product=product,)
        if cart_item.exists():
            cart_item = CartItem.objects.first()
            cart_item.quantity = quantity
            return cart_item
        cart_item = CartItem.objects.create(cart=cart, product=product, quantity=quantity)
        cart.cart_items.add(cart_item)
        return cart_item


class CartSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()
    total_price = serializers.SerializerMethodField()
    number_of_items = serializers.SerializerMethodField()
    cart_items = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = '__all__'

    def get_total_price(self, object):
        return object.total_price

    def get_number_of_items(self, object):
        return object.number_of_items



