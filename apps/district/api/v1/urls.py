from django.urls import path
from .views import DistrictListCreateAPIView,DistrictRetrieveUpdateDestroyAPIView

urlpatterns = [
    path("api/v1/district",DistrictListCreateAPIView.as_view(), name="district"),
    path(
        "api/v1/district/<int:pk>",
       DistrictRetrieveUpdateDestroyAPIView.as_view(),
        name="district",
    ),
]
