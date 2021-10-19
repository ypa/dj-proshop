from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path("users/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("", views.get_routes, name="routes"),
    path("products/", views.get_products, name="products"),
    path("products/<str:pk>", views.get_product, name="product"),
]
