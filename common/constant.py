from django_filters import rest_framework as filters
class NumberInFilter(filters.BaseInFilter, filters.NumberFilter):
    pass

class CharInFilter(filters.BaseInFilter, filters.CharFilter):
    pass

class ValidateInputFilterSet(filters.FilterSet):
    def __init__(self, *args, **kwargs):
        data = kwargs.get('data', None)
        if data:
            data = data.copy()
            keys_to_remove = []
            for key, value in data.items():
                if value == 'NaN' or (isinstance(value, str) and not value.isdigit()):
                    keys_to_remove.append(key)
            for key in keys_to_remove:
                data.pop(key)
            kwargs['data'] = data
        super().__init__(*args, **kwargs)
