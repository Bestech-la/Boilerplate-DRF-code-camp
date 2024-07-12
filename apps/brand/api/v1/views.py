
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.parsers import FormParser, MultiPartParser

from apps.brand.api.v1.filters import BrandFilterSet
from faker import Faker
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
import random
import requests
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db import transaction

from apps.brand.models import Brand
from .serializers import BrandSerializer

from .serializers import BrandSerializer


class BrandListCreateAPIView(ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    filterset_class = BrandFilterSet
    parser_classes = (MultiPartParser, FormParser)


class BrandRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    parser_classes = (MultiPartParser, FormParser)

    from django.utils import timezone


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

class GenerateMockBrand(APIView):
    @transaction.atomic
    def post(self, request, *args, **kwargs):
        for i in range(15):  # Adjust the range for the number of mock brands you want to create
            title = fake.company()
            description = fake.text()
            is_popular = random.choice([True, False])
            logo_url = random.choice(image_urls)
            logo_file = download_image(logo_url, f"brand{i}.jpg")

            brand = Brand(
                title=title,
                description=description,
                is_popular=is_popular,
            )
            if logo_file:
                brand.logo.save(f"brand{i}.jpg", logo_file)
            brand.save()
        return Response({"status": "success", "message": "15 mock brands created."})
