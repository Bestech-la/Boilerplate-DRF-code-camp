from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from apps.district.models import District
from apps.profile.api.v1.filter import ProfileFilterSet
from apps.profile.api.v1.serializers import ProfileSerializer
from apps.profile.models import Profile
from common.access_control.authorization import CasbinAuthorization
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.parsers import MultiPartParser, FormParser
import random
from faker import Faker
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.profile.models import Profile, Gender
from django.utils import timezone
import requests
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile



class ProfileListCreateAPIView(ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProfileFilterSet
    search_fields = ["fullname", "nickname", "gender"]
    ordering_fields = ["fullname", "nickname", "gender",]
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [CasbinAuthorization]

class ProfileRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [CasbinAuthorization]


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

MAX_FULLNAME_LENGTH = 255
MAX_NICKNAME_LENGTH = 255

def download_image(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        img_temp = NamedTemporaryFile(delete=True)
        img_temp.write(response.content)
        img_temp.flush()
        return File(img_temp, name=save_path)
    return None

class GenerateMockProfiles(APIView):
    def post(self, request, *args, **kwargs):
        districts = District.objects.all()
        for i in range(17):
            fullname = fake.name()[:MAX_FULLNAME_LENGTH]
            nickname = fake.first_name()[:MAX_NICKNAME_LENGTH]
            image_url = random.choice(image_urls)
            image_file = download_image(image_url, f"profile{i}.jpg")
            district = random.choice(districts)

            profile = Profile(
                fullname=fullname,
                nickname=nickname,
                phone=fake.msisdn()[:15],  # Ensure phone number length does not exceed 15 characters
                gender=random.choice([gender.value for gender in Gender]),
                age=random.randint(18, 60),
                birthday=fake.date_of_birth(tzinfo=None, minimum_age=18, maximum_age=60),
                date_added=timezone.now(),
                district=district,
            )
            if image_file:
                profile.image.save(f"profile{i}.jpg", image_file)
            profile.save()
        return Response({"status": "success", "message": "17 mock profiles created."})