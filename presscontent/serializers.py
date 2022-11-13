from rest_framework import serializers
from presscontent.models import PressContent


class PressContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PressContent
        fields = ['pk', 'label', 'url', 'date']

    url = serializers.SerializerMethodField()

    def get_url(self, obj):
        obj_url = obj.get_current_site(self.context["request"])
        return obj_url
