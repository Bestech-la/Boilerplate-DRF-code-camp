from rest_flex_fields import FlexFieldsModelSerializer
from apps.category.models import Category, CategoryProduct

class CategorySerializer(FlexFieldsModelSerializer):

    class Meta:
        model = Category
        fields =  ['id', "title", 'description', 'updated_on', 'created_on']

class CategoryProductSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = CategoryProduct
        fields =  ['id', "title", "category", "product", 'updated_on', 'created_on']