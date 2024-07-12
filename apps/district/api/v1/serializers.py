from rest_framework import serializers
from apps.district.models import District
from rest_flex_fields import FlexFieldsModelSerializer


class DistrictSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = District
        fields = ["id", "province_name", "district_name",]
