from rest_flex_fields import FlexFieldsModelSerializer
from sorl_thumbnail_serializer.fields import HyperlinkedSorlImageField

from apps.book.models import Book, Publisher


class BookSerializer(FlexFieldsModelSerializer):
    thumbnail = HyperlinkedSorlImageField(
        "128x128", options={"crop": "center"}, source="image", read_only=True
    )

    class Meta:
        model = Book
        fields = ["title", "image", "publisher", "isbn", "publicationDate", "price", "stock", "thumbnail"]

class PublisherSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Publisher
        fields = [
            "name",
            "address",
        ]
