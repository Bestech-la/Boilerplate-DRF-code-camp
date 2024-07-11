from django.contrib.auth.models import User, Group
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("name",)


class UserSerializer(FlexFieldsModelSerializer):
    groups = serializers.ListSerializer(child=serializers.CharField())
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "is_active",
            "date_joined",
            "groups",
            "password",
        )

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret.pop('password', None)
        return ret

    def to_internal_value(self, data):
        if "groups" in data:
            group_names = data.pop("groups")
            group_ids = list(
                Group.objects.filter(name__in=group_names).values_list("id", flat=True)
            )
            data["groups"] = group_ids
        return super().to_internal_value(data)

    def create(self, validated_data):
        groups_data = validated_data.pop("groups", None)
        user = User.objects.create_user(**validated_data)
        if groups_data is not None:
            user.groups.set(groups_data)
        return user

    def update(self, instance, validated_data):
        groups_data = validated_data.pop("groups", None)
        if groups_data is not None:
            instance.groups.set(groups_data)
        return super().update(instance, validated_data)
