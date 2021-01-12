from django.urls import path, include

from rest_framework import routers
from rest_framework.routers import DefaultRouter

from cart.api.views import CartView

router = DefaultRouter()

router.register(r'', CartView, basename="Cart")
# router.register(r'item', CartItemView, basename='CartItem')

urlpatterns = [
    path('', include(router.urls)),
]