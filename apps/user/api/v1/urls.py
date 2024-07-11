from django.urls import path
from .views import ListCreateUserView, RetrieveUpdateDestroyUserView

urlpatterns = [
    path('api/v1/user', ListCreateUserView.as_view(), name='user'),
    path('api/v1/user/<int:pk>', RetrieveUpdateDestroyUserView.as_view(), name='user'),
]
