from rest_framework.viewsets import GenericViewSet
from drf_aggregation.mixins import AggregationMixin
from drf_aggregation.helpers import get_aggregation
from rest_framework.response import Response
from django.core.paginator import Paginator
from rest_framework.exceptions import ValidationError
from enum import Enum
from django.db.models import Func, F

class Cast(Func):
    """
    Custom database function to cast a field to a different type in SQL queries.
    Attributes:
    function (str): The SQL function to use (CAST).
    template (str): The template for the SQL function.
    """
    function = 'CAST'
    template = '%(function)s(%(expressions)s AS %(type)s)'

FIELD_TYPE_MAPPING = {
    'ot': 'NUMERIC', 
}
    
class AggregationViewSet(AggregationMixin, GenericViewSet):
    def aggregation(self, request):
        params = request.query_params
        aggregation = params.get("aggregation", None)
        if not aggregation:
            raise ValidationError({"error": "'aggregation' is required"})
        aggregation_field = params["aggregationField"].replace(".", "__") if "aggregationField" in params else None
        
        # Check if the field is numeric and needs casting
        if aggregation_field in FIELD_TYPE_MAPPING:
                field_type = FIELD_TYPE_MAPPING[aggregation_field]
                aggregation_field = Cast(F(aggregation_field), type=field_type)

        limit_by = params["limitBy"].replace(".", "__") if "limitBy" in params else None
        result = get_aggregation(
            queryset=self.filter_queryset(self.get_queryset()),
            aggregation=aggregation,
            aggregation_field=aggregation_field,
            percentile=params.get("percentile", None),
            additional_filter=params.get("additionalFilter", None),
            group_by=self._get_group_by(request),
            order_by=self._get_order_by(request),
            limit=int(params.get("limit", 0)),
            limit_by=limit_by,
            limit_show_other=params.get("showOther", None) == "1",
            limit_other_label=params.get("otherGroupName", None)
        )
        paginated_response = self._get_paginated_response(request, result)
        return Response(paginated_response)

    def _get_paginated_response(self, request, result):
        page_size = int(request.query_params.get('page_size', self.pagination_class.page_size))
        if isinstance(result, list):
            page_number = request.query_params.get(self.pagination_class.page_query_param, 1)
            paginator = Paginator(result, page_size)
            page = paginator.get_page(page_number)
            paginated_response = {
                'count': paginator.count,
                'next': page.has_next(),
                'previous': page.has_previous(),
                'results': list(page)
            }
        else:  
            paginated_response = {
                'count': 1,
                'next': False,
                'previous': False,
                'results': result
            }
        return paginated_response

class AGGREGATION_OPERATION(Enum):
    SUM = "sum"
    AVG = "average"
    COUNT = "count"
    MINIMUM = "minimum"
    MAXIMUM = "maximum"
    
    @classmethod
    def choices(cls):
        """Return choices as a list of tuples."""
        return [(operation.value, operation.name.replace("_", " ").title()) for operation in cls]