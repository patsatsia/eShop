from django.urls import path, include

from rest_framework import routers
from rest_framework.routers import DefaultRouter

from cart.api.views import CartItemView

router = DefaultRouter()
router.register(r"", CartItemView)

urlpatterns = [
    path("", include(router.urls))
]