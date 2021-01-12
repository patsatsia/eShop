from django.urls import path, include

urlpatterns = [
    path("accounts/", include("authentication.api.urls")),
    path("category/", include("category.api.urls")),
    path("products/", include("products.api.urls")),
    path('favorites/', include('favorites.api.urls')),
    path('cart/', include('cart.api.urls')),
]