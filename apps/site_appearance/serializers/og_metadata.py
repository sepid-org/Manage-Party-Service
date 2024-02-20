from rest_framework import serializers
from apps.site_appearance.models import OpenGraphMetaData


class OpenGraphMetadataSerializer(serializers.ModelSerializer):

    class Meta:
        model = OpenGraphMetaData
        fields = ['title', 'type', 'image', 'url']
