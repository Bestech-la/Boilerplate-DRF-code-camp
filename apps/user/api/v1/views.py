from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from common.access_control.authorization import CasbinAuthorization
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.response import Response

class ListCreateUserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['username', 'is_active']
    search_fields = ['username', 'is_active']
    ordering_fields = ['username', 'is_active']
    permission_classes = [CasbinAuthorization]


class RetrieveUpdateDestroyUserView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [CasbinAuthorization]
    
    def patch(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            password = serializer.validated_data.pop('password', None)
            if password is not None:
                user.set_password(password)
            serializer.save()
            if password:
                return Response({"message": "User and password updated successfully."}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "User updated successfully."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
