from django_filters import rest_framework as filters
from apps.profile.models import Profile
from common.constant import NumberInFilter


class ProfileFilterSet(filters.FilterSet):
    id = NumberInFilter(field_name="id", lookup_expr="in")
    class Meta:
        model = Profile
        fields = ["fullname", "nickname", "gender"]
