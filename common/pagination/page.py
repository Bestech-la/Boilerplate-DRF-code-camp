from rest_framework import pagination
from rest_framework.response import Response
from django_filters import BooleanFilter

class PageWithTotalPage(pagination.PageNumberPagination):
    page_size = 10 
    page_size_query_param = 'page_size'
    max_page_size = 100 
    def paginate_queryset(self, queryset, request, view=None):
        paginate = request.query_params.get('paginate')
        if paginate is not None and paginate.lower() == 'false':
            self.request = request
            return list(queryset)
        return super().paginate_queryset(queryset, request, view)
    
    def get_paginated_response(self, data):
        if 'paginate' in self.request.query_params and self.request.query_params['paginate'].lower() == 'false':
            return self._get_non_paginated_response(data)
        return self._get_paginated_response(data)

    def _get_non_paginated_response(self, data):
        return Response({
            'links': {
                'next': None, 
                'previous': None
            },
            'count': len(data),
            'results': data 
        })

    def _get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'results': data
        })

def filter_paginate(queryset, name, value):
    return queryset

PaginateFilter = BooleanFilter(method=filter_paginate, label='Paginate')
