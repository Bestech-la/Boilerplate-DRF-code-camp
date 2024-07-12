from apps.brand.models import Brand
from common.camel_case.serializer import CamelCaseSerializer


class BrandSerializer(CamelCaseSerializer):
    class Meta:
        model = Brand
        fields = '__all__'
