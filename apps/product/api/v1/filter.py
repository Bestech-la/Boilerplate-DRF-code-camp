from django_filters import rest_framework as filters
from apps.product.models import Product
from common.constant import NumberInFilter

class ProductFilterSet(filters.FilterSet):
    id = NumberInFilter(field_name='id', lookup_expr='in')
    class Meta:
        model = Product
        fields = [
            "name",
            "price",
            "size",
            "stock",
            "brand",
            "type"
        ]

