from rest_framework.generics import (ListAPIView, RetrieveAPIView, get_object_or_404)
from pagecontent_api.models import PressContent
from pagecontent_api.serializers import PressContentSerializer
from pagecontent_api.pagination import PressContentPagination


class PressContentListAPIView(ListAPIView):
    queryset = PressContent.objects.all()
    serializer_class = PressContentSerializer
    pagination_class = PressContentPagination


class PressContentDetailAPIView(RetrieveAPIView):
    queryset = PressContent.objects.all()
    serializer_class = PressContentSerializer
    lookup_field = 'pk'


