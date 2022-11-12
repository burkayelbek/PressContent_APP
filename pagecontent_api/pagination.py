from rest_framework.pagination import PageNumberPagination


class PressContentPagination(PageNumberPagination):
    page_size = 4
