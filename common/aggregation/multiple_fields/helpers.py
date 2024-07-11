from django.db import models
from rest_framework.exceptions import ValidationError
from drf_complex_filter.utils import ComplexFilter
from drf_aggregation.aggregates import Percentile
from .aggregation import Aggregation
from drf_aggregation.utils import Aggregator
import re


def get_aggregation(
    queryset: models.QuerySet,
    aggregations: list,
    group_by: list = None,
    order_by: list = None,
    limit: int = 0,
    limit_by: str = None,
    limit_show_other: bool = False,
    limit_other_label: str = None,
):
    aggregator = Aggregator(queryset=queryset)
    annotations = {}
    for agg in aggregations:
        aggregation = agg['aggregation']
        aggregation_field = agg['field']
        percentile = agg.get('percentile')
        additional_filter = agg.get('additional_filter')

        annotation_name = f"{aggregation}__{aggregation_field}"
        annotations[annotation_name] = get_annotation(
            aggregation=aggregation,
            aggregation_field=aggregation_field,
            percentile=percentile,
            additional_filter=additional_filter,
            queryset=queryset,
        )
    return aggregator.get_database_aggregation(
        annotations=annotations,
        group_by=group_by,
        order_by=order_by,
        limit=limit,
        limit_by=limit_by,
        limit_show_other=limit_show_other,
        limit_other_label=limit_other_label,
    )


def get_annotation(
    aggregation: str,
    aggregation_field: str = None,
    percentile: str = None,
    queryset: models.QuerySet = None,
    additional_filter: str = None,
) -> dict:
    if aggregation == Aggregation.COUNT.value:
        return models.Count('id')

    if aggregation == Aggregation.PERCENT.value:
        if not additional_filter:
            raise ValidationError({"error": "'additionalFilter' is required for 'aggregation=percent'"}, code=422)

        complex_filter = ComplexFilter(model=queryset.model)
        additional_query, _ = complex_filter.generate_from_string(additional_filter)
        if not additional_query:
            raise ValidationError({"error": "Additional filter cannot be empty"}, code=422)

        return models.ExpressionWrapper(
            models.F("numerator") * 1.0 / models.F("denominator"),
            output_field=models.FloatField()
        )

    if not aggregation_field:
        raise ValidationError({"error": f"'aggregationField' is required for 'aggregation={aggregation}'"}, code=422)

    if aggregation == Aggregation.DISTINCT.value:
        return models.Count(aggregation_field, distinct=True)

    if aggregation == Aggregation.SUM.value:
        return models.Sum(aggregation_field)

    if aggregation == Aggregation.AVERAGE.value:
        return models.Avg(aggregation_field)

    if aggregation == Aggregation.MIN.value:
        return models.Min(aggregation_field)

    if aggregation == Aggregation.MAX.value:
        return models.Max(aggregation_field)

    if aggregation == Aggregation.PERCENTILE.value:
        if not percentile:
            raise ValidationError({"error": "'percentile' is required for 'aggregation=percentile'"}, code=422)

        model: models.Model = queryset.model
        field = None
        for field_name in aggregation_field.split("__"):
            field = getattr(field, field_name) if field else model._meta.get_field(field_name)

        if field.get_internal_type() != "FloatField":
            return Percentile(aggregation_field, percentile, output_field=models.FloatField())
        return Percentile(aggregation_field, percentile)

    raise ValidationError({"error": "Unknown value for param 'aggregation'"}, code=422)


def transform_aggregation_dict(agg_dict):
    result = []
    aggregation_types = ['sum', 'count', 'average', 'min', 'max', 'percent', 'percentile']
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

def get_sql_type(field):
    field_instance = field.get_internal_type()
    if field_instance in ('IntegerField', 'FloatField', 'DecimalField'):
        return 'NUMERIC'
    elif field_instance == 'CharField':
        return 'TEXT'
    elif field_instance == 'BooleanField':
        return 'BOOLEAN'
    # Add other field types as needed
    return None

def sanitize_alias(alias):
    """Sanitize the alias to remove any invalid characters."""
    return re.sub(r'\W|^(?=\d)', '_', alias)