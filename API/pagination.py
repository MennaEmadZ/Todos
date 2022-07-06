from rest_framework import pagination
from rest_framework.response import Response


class CustomPagination(pagination.LimitOffsetPagination):
    default_limit = 20
    limit_query_param = '_start'
    offset_query_param = '_limit'

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'X-Total-Count': len(data),
            'results': data
        })