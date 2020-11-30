from django.urls import path, include

urlpatterns = [
    path("accounts/", include("authentication.api.urls")),
    path("category/", include("category.api.urls"))
]