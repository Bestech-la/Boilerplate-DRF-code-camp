
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from apps.category.api.v1.filter import CategoryFilterSet, CategoryProductFilterSet
from apps.category.models import Category, CategoryProduct
from common.post_list.views import swagger_post_list, post

from .serializers import CategoryProductSerializer, CategorySerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db import transaction
from faker import Faker
fake = Faker()

class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filterset_class = CategoryFilterSet
    search_fields = ["title", "description"]
    ordering_fields =  ["title", "description"]
    
class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryProductListCreateAPIView(ListCreateAPIView):
    queryset = CategoryProduct.objects.all()
    serializer_class = CategoryProductSerializer
    filterset_class = CategoryProductFilterSet
    search_fields = ["title", "category", "product"]
    ordering_fields =  ["title", "category", "product"]
    
    @swagger_post_list("CategoryProductSerializer", CategoryProductSerializer)
    def post(self, request, *args, **kwargs):
        return post(self, CategoryProduct, request, *args, **kwargs)

class CategoryProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = CategoryProduct.objects.all()
    serializer_class = CategoryProductSerializer
    



class GenerateMockCategoryListCreateAPIView(APIView):
    @transaction.atomic
    def post(self, request, *args, **kwargs):
        for i in range(15):
            title = fake.word().title()
            description = fake.text()
            category = Category(
                title=title,
                description=description,
            )
            category.save()
        return Response({"status": "success", "message": "15 mock categories created."})