from django_filters import rest_framework as filters
from apps.profile.models import Profile, ProfileAddress
from common.constant import NumberInFilter


class ProfileFilterSet(filters.FilterSet):
    id = NumberInFilter(field_name="id", lookup_expr="in")
    class Meta:
        model = Profile
        fields = ["fullname", "nickname", "gender"]


class ProfileAddressFilterSet(filters.FilterSet):
    id = NumberInFilter(field_name="id", lookup_expr="in")
    profile = NumberInFilter(field_name="profile", lookup_expr="in")
    district = NumberInFilter(field_name="district", lookup_expr="in")
    class Meta:
        model = ProfileAddress
        fields = ["village", "type", "profile", "district"]
