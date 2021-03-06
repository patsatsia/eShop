from django.urls import path, include
from .views import CategoryView

from rest_framework import routers
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', CategoryView)

urlpatterns = [
    path("", include(router.urls))
]