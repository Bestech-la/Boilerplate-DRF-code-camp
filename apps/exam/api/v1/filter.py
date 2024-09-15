from django_filters import rest_framework as filters

from apps.exam.models import Exam, Subject


class CharInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class SubjectFilterSet(filters.FilterSet):
    id = CharInFilter(field_name="id", lookup_expr="in")

    class Meta:
        model = Subject
        fields = ["name", "code"]


class ExamFilterSet(filters.FilterSet):
    id = CharInFilter(field_name="id", lookup_expr="in")

    class Meta:
        model = Exam
        fields = [
            "title",
            "subject",
            "examType",
            "maxScore",
        ]
