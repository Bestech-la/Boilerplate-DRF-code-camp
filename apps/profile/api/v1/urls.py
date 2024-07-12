from django.urls import path
from .views import (
    GenerateMockProfiles,
    ProfileListCreateAPIView,
    ProfileRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path( "api/v1/profile", ProfileListCreateAPIView.as_view(), name="profile", ),
    path( "api/v1/profile/<int:pk>", ProfileRetrieveUpdateDestroyAPIView.as_view(), name="profile", ),
    path("api/v1/profile/generate-mock", GenerateMockProfiles.as_view(), name="generate-mock-profiles"),
]