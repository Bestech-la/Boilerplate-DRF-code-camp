from django.urls import path

from .views import BrandListCreateAPIView, BrandRetrieveUpdateDestroyAPIView, GenerateMockBrand

urlpatterns = [
    path('api/v1/brand', BrandListCreateAPIView.as_view(),name='brand'),
    path('api/v1/brand/<int:pk>', BrandRetrieveUpdateDestroyAPIView.as_view(),name='brand'),
    path('api/v1/brand/generate-mock', GenerateMockBrand.as_view(), name='generate-mock-brand'),
]