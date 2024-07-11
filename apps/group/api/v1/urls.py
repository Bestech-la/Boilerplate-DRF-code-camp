from django.urls import path
from .views import ListCreateUserView, RetrieveUpdateDestroyUserView

urlpatterns = [
    path('api/v1/group', ListCreateUserView.as_view(), name='group'),
    path('api/v1/group/<int:pk>', RetrieveUpdateDestroyUserView.as_view(), name='group'),
]
