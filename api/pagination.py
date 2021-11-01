from rest_framework.pagination import LimitOffsetPagination


class CustomLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 1
    limit_query_param = 'mylimit'
    offset_query_param = 'myoffset'
    max_limit = 4
