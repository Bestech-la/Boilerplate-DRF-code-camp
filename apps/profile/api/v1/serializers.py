
from rest_flex_fields import FlexFieldsModelSerializer
from sorl_thumbnail_serializer.fields import HyperlinkedSorlImageField

from apps.profile.models import Profile

class ProfileSerializer(FlexFieldsModelSerializer):
    thumbnail = HyperlinkedSorlImageField("128x128", options={"crop": "center"}, source="image", read_only=True)
    class Meta:
        model = Profile
        fields = ["id", "fullname", "nickname", "gender", "birthday", "image", "age", "thumbnail", "date_added", "district"]