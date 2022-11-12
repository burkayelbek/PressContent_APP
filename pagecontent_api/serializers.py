from rest_framework.serializers import ModelSerializer
from pagecontent_api.models import PressContent


class PressContentSerializer(ModelSerializer):
    class Meta:
        model = PressContent
        exclude = ('id', 'created', 'modified')
        lookup_field = 'pk'
