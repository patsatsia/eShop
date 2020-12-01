from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from products.api.views import ProductView

router = DefaultRouter()
router.register(r'', ProductView)


urlpatterns = [
    path("", include(router.urls))
]