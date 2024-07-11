from django.urls import path
from .views import (
    GenerateMockProducts,
    ProductListCreateAPIView,
    ProductRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path( "api/v1/product", ProductListCreateAPIView.as_view(), name="product", ),
    path( "api/v1/product/<int:pk>", ProductRetrieveUpdateDestroyAPIView.as_view(), name="product", ),
    path("api/v1/product/generate-mock", GenerateMockProducts.as_view(), name="generate-mock-products"),
]
