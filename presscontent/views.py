from rest_framework.generics import (ListAPIView, RetrieveAPIView)
from presscontent.models import PressContent
from presscontent.serializers import PressContentSerializer
from presscontent.pagination import PressContentPagination
from rest_framework.filters import OrderingFilter
from django.http import HttpResponse


class PressContentListAPIView(ListAPIView):
    queryset = PressContent.objects.all()
    serializer_class = PressContentSerializer
    pagination_class = PressContentPagination
    filter_backends = [OrderingFilter]


class PressContentDetailAPIView(RetrieveAPIView):
    queryset = PressContent.objects.all()
    serializer_class = PressContentSerializer
    lookup_field = 'slug'

