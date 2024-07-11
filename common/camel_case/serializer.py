from rest_flex_fields import FlexFieldsModelSerializer
import re
class CamelCaseSerializer(FlexFieldsModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        camel_case_data = {}
        for snake_case_key, value in data.items():
            camel_case_key = re.sub(r'(?!^)_([a-zA-Z])', lambda m: m.group(1).upper(), snake_case_key)
            camel_case_data[camel_case_key] = value
        return camel_case_data

    def to_internal_value(self, data):
        snake_case_data = {}
        for camel_case_key, value in data.items():
            snake_case_key = re.sub(r'(?<!^)(?=[A-Z])', '_', camel_case_key).lower()
            snake_case_data[snake_case_key] = value
        return super().to_internal_value(snake_case_data)