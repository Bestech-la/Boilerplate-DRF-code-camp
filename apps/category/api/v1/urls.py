from django.urls import path

from .views import CategoryListCreateAPIView, CategoryProductListCreateAPIView, CategoryProductRetrieveUpdateDestroyAPIView, CategoryRetrieveUpdateDestroyAPIView, GenerateMockCategoryListCreateAPIView

urlpatterns = [
    path('api/v1/category', CategoryListCreateAPIView.as_view(),name='category'),
    path('api/v1/category/<int:pk>', CategoryRetrieveUpdateDestroyAPIView.as_view(),name='category'),
    path('api/v1/category/category-product', CategoryProductListCreateAPIView.as_view(),name='category-product'),
    path('api/v1/category/category-product/<int:pk>', CategoryProductRetrieveUpdateDestroyAPIView.as_view(),name='category-product'),
    path('api/v1/category/generate-mock', GenerateMockCategoryListCreateAPIView.as_view(), name='generate-mock-category'),
]
