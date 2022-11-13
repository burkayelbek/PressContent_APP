from rest_framework import generics
from presscontent.models import PressContent
from presscontent.serializers import PressContentSerializer
from presscontent.pagination import PressContentPagination
from rest_framework.filters import OrderingFilter
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer


class PressContentListAPIView(generics.ListAPIView):
    renderer_classes = [JSONRenderer, TemplateHTMLRenderer]
    template_name = 'list.html'
    queryset = PressContent.objects.all()
    serializer_class = PressContentSerializer
    pagination_class = PressContentPagination
    filter_backends = [OrderingFilter]


class PressContentDetailAPIView(generics.RetrieveAPIView):
    renderer_classes = [JSONRenderer, TemplateHTMLRenderer]
    template_name = 'detail.html'
    queryset = PressContent.objects.all()
    serializer_class = PressContentSerializer
    lookup_field = 'slug'

