from rest_framework import serializers
from presscontent.models import PressContent


class PressContentSerializer(serializers.ModelSerializer):
    #url = serializers.SerializerMethodField()

    class Meta:
        model = PressContent
        fields = [
            'pk',
            'label',
            'slug',
            #'url',
            'date']
