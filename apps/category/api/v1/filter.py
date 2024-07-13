from django_filters import rest_framework as filters
from apps.category.models import Category, CategoryProduct
from common.constant import NumberInFilter

class CategoryFilterSet(filters.FilterSet):
    id = NumberInFilter(field_name='id', lookup_expr='in')
    class Meta:
        model = Category
        fields = ["id"]

class CategoryProductFilterSet(filters.FilterSet):
    id = NumberInFilter(field_name='id', lookup_expr='in')
    category = NumberInFilter(field_name='category', lookup_expr='in')
    product = NumberInFilter(field_name='product', lookup_expr='in')
    class Meta:
        model = CategoryProduct
        fields = ["id","title","category","product"]




