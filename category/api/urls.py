from django.urls import path, include
from .views import CategorySerializerView

from rest_framework import routers
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', CategorySerializerView)

urlpatterns = [
    path("", include(router.urls))
]