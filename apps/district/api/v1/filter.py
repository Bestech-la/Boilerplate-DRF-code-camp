from django_filters import rest_framework as filters
from django.db.models import Subquery, OuterRef, Q
from apps.district.models import District

class CharInFilter(filters.BaseInFilter, filters.CharFilter):
    pass

class DistrictFilterSet(filters.FilterSet):
    province = CharInFilter(field_name='province_name', lookup_expr='in')
    class Meta:
        model = District
        fields = ["id", "province_name"]

    def get_first_record_per_province(self, queryset):
        min_id_subquery = District.objects.filter(
            province_name=OuterRef('province_name')
        ).order_by('id').values('id')[:1]

        return queryset.filter(id__in=Subquery(min_id_subquery))

    @property
    def qs(self):
        parent = super().qs
        province_names = self.request.GET.get('province')
        if province_names:
            province_list = province_names.split(',')
            parent = self.get_first_record_per_province(parent)
            parent = parent.filter(province_name__in=province_list)
        return parent
