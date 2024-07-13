from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from apps.brand.models import Brand
from apps.product.api.v1.filter import ProductFilterSet
from apps.product.api.v1.serializers import ProductSerializer
from apps.product.models import Product, Type
from common.access_control.authorization import CasbinAuthorization
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.parsers import MultiPartParser, FormParser
import random
from faker import Faker
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
import requests

class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilterSet
    search_fields = ["name", "price", "size", "stock", "type"]
    ordering_fields = ["name", "price", "size", "stock", "type"]
    parser_classes = (MultiPartParser, FormParser)
    # permission_classes = [CasbinAuthorization]

class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    parser_classes = (MultiPartParser, FormParser)
    # permission_classes = [CasbinAuthorization]

fake = Faker()
image_urls = [
    "https://picsum.photos/200/300?random=1",
    "https://picsum.photos/200/300?random=2",
    "https://picsum.photos/200/300?random=3",
    "https://picsum.photos/200/300?random=4",
    "https://picsum.photos/200/300?random=5",
    "https://picsum.photos/200/300?random=6",
    "https://picsum.photos/200/300?random=7",
    "https://picsum.photos/200/300?random=8",
    "https://picsum.photos/200/300?random=9",
    "https://picsum.photos/200/300?random=10",
    "https://picsum.photos/200/300?random=11",
    "https://picsum.photos/200/300?random=12",
    "https://picsum.photos/200/300?random=13",
    "https://picsum.photos/200/300?random=14",
    "https://picsum.photos/200/300?random=15",
    "https://picsum.photos/200/300?random=16",
    "https://picsum.photos/200/300?random=17",
]
def download_image(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        img_temp = NamedTemporaryFile(delete=True)
        img_temp.write(response.content)
        img_temp.flush()
        return File(img_temp, name=save_path)
    return None

class GenerateMockProducts(APIView):
    def post(self, request, *args, **kwargs):
        brands = Brand.objects.all()
        product_types = [product_type.value for product_type in Type]
        for i in range(17):
            name = fake.word()
            price = round(random.uniform(10.0, 100.0), 2)
            size = str(random.choice([36, 37, 38, 39, 40, 41, 42, 43]))
            stock = random.randint(1, 100)
            image_url = random.choice(image_urls)
            image_file = download_image(image_url, f"product{i}.jpg")
            product_type = random.choice(product_types)
            brand = random.choice(brands)  # Randomly select a brand from available brands

            product = Product(
                name=name,
                price=price,
                size=size,
                stock=stock,
                image=image_file,
                type=product_type,
                brand=brand,
                date_added=timezone.now()
            )
            product.save()
        
        return Response({"status": "success", "message": "17 mock products created."})
    