from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from favorites.api.views import FavProductView

router = DefaultRouter()
router.register(r'', FavProductView, basename='FavProduct')


urlpatterns = [
    path("", include(router.urls))
]