from django_filters import rest_framework as filters

from apps.brand.models import Brand

class BrandFilterSet(filters.FilterSet):    
    class Meta:
        model = Brand
        fields = {
            'is_popular'
        }