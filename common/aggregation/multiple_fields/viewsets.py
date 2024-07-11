from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from django.core.paginator import Paginator
from drf_aggregation.mixins import AggregationMixin
from .helpers import get_aggregation
from .aggregation import Aggregation

def transform_aggregation_dict(agg_dict):
  result = []
  aggregation_types = [ 'sum', 'count', 'average', 'min', 'max', 'percent', 'percentile' ]
  for agg_type in aggregation_types:
    key = f'aggregate[{agg_type}]'
    if key in agg_dict:
      fields = agg_dict[key].split(',')
      result.extend({
        'aggregation': agg_type,
        'field': field,
        'percentile': None
      } for field in fields)
  return result


class AggregationViewSet(AggregationMixin, GenericViewSet):
    def aggregation(self, request):
        params = request.query_params
        aggregations_list = transform_aggregation_dict(params)
        if not aggregations_list:
            raise ValidationError({"error": "'aggregate' is required"})
        
        aggregation_map = {
            'count': Aggregation.COUNT.value,
            'sum': Aggregation.SUM.value,
            'average': Aggregation.AVERAGE.value,
            'min': Aggregation.MIN.value,
            'max': Aggregation.MAX.value,
            'distinct': Aggregation.DISTINCT.value,
            'percent': Aggregation.PERCENT.value,
            'percentile': Aggregation.PERCENTILE.value
        }

        for agg in aggregations_list:
            agg['aggregation'] = aggregation_map.get(agg['aggregation'].lower())

        limit_by = params.get("limitBy", None)
        if limit_by:
            limit_by = limit_by.replace(".", "__")

        result = get_aggregation(
            queryset=self.filter_queryset(self.get_queryset()),
            aggregations=aggregations_list,  # List of aggregations
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
        formatted_results = self.format_results(result)
        page_size = int(request.query_params.get('page_size', self.pagination_class.page_size))
        if isinstance(formatted_results, list):
            page_number = request.query_params.get(self.pagination_class.page_query_param, 1)
            paginator = Paginator(formatted_results, page_size)
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
                'results': formatted_results
            }
        return paginated_response

    def format_results(self, result):
        formatted_results = []

        if isinstance(result, list):
            for item in result:
                formatted_item = self.format_item(item)
                formatted_results.append(formatted_item)
        else:
            formatted_results = self.format_item(result)

        return formatted_results

    def format_item(self, item):
        formatted_item = {}
        for key, value in item.items():
            if "__" in key:
                aggregation, field = key.split("__", 1)
                if aggregation not in formatted_item:
                    formatted_item[aggregation] = {}
                formatted_item[aggregation][field] = value
            else:
                formatted_item[key] = value
        return formatted_item

    @staticmethod
    def _get_group_by(request) -> list:
        group_by = request.query_params.get("groupBy", None)
        group_by = group_by.split(",") if group_by else []
        return [field.replace(".", "__") for field in group_by]

    @staticmethod
    def _get_order_by(request) -> list:
        order_by = request.query_params.get("orderBy", None)
        order_by = order_by.split(",") if order_by else []
        return [field.replace(".", "__") for field in order_by]
    
# http://127.0.0.1:8000/api/v1/attendance/aggregation?aggregate[sum]=ot&aggregate[count]=user&groupBy=user&type=on_time