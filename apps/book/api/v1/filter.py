from django_filters import rest_framework as filters

from apps.book.models import Book, Publisher


class CharInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class BookFilterSet(filters.FilterSet):
    id = CharInFilter(field_name="id", lookup_expr="in")

    class Meta:
        model = Book
        fields = ["title", "publisher", "isbn", "publicationDate", "price", "stock"]


class PublisherFilterSet(filters.FilterSet):
    id = CharInFilter(field_name="id", lookup_expr="in")

    class Meta:
        model = Publisher
        fields = [
            "name",
            "address",
        ]
