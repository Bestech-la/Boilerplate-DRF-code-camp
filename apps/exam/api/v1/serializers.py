from rest_flex_fields import FlexFieldsModelSerializer
from sorl_thumbnail_serializer.fields import HyperlinkedSorlImageField

from apps.exam.models import Exam, Subject


class SubjectSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Subject
        fields = ["name", "code", "id",]

class ExamSerializer(FlexFieldsModelSerializer):
    thumbnail = HyperlinkedSorlImageField(
        "128x128", options={"crop": "center"}, source="image", read_only=True
    )
    class Meta:
        model = Exam
        fields = [
            "id",
            "subject",
            "examType",
            "examDate",
            "maxScore",
            "image",
            "thumbnail",
        ]
