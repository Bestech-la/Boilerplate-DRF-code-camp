
from rest_flex_fields import FlexFieldsModelSerializer
from apps.product.models import Product
from sorl_thumbnail_serializer.fields import HyperlinkedSorlImageField

class ProductSerializer(FlexFieldsModelSerializer):
    thumbnail = HyperlinkedSorlImageField("128x128", options={"crop": "center"}, source="image", read_only=True)
    class Meta:
        model = Product
        fields = ["id", "name", "price", "size",  "stock", "image", "date_added", "thumbnail", "brand", "type"]

        