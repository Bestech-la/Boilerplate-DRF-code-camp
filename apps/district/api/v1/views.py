from rest_framework import status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from apps.district.api.v1.serializers import DistrictSerializer

from apps.district.models import District
from .filter import DistrictFilterSet
from common.access_control.authorization import CasbinAuthorization




class DistrictListCreateAPIView(ListCreateAPIView):
    """
    ---
    # Testing Notes
    - Passes DistrictListCreateAPIView API tests: {api_tests_passed}
    - Test Coverage: {test_coverage}%
    ---
    """
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = DistrictFilterSet
    permission_classes = [CasbinAuthorization]

    @swagger_auto_schema(
        operation_description="post single or list of districts",
        request_body=DistrictSerializer(many=True),
        responses={status.HTTP_201_CREATED: DistrictSerializer(many=True)},
    )
    def post(self, request, *args, **kwargs):
        is_many = isinstance(request.data, list)
        if not is_many:
            return super().create(request, *args, **kwargs)
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        queryset = District.objects.all()
        return queryset


class DistrictRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    ---
    # Testing Notes
    - Passes DistrictRetrieveUpdateDestroyAPIView API tests: {api_tests_passed}
    - Test Coverage: {test_coverage}%
    ---
    """
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    permission_classes = [CasbinAuthorization]
