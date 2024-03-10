from rest_framework import serializers
from apps.party.models import OpenGraphMetaData
from apps.party.serializers.logo_serializer import get_media_url


class OpenGraphMetadataSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = OpenGraphMetaData
        fields = ['title', 'description', 'type', 'image', 'url']

    def get_image(self, obj):
        return get_media_url() + obj.image.url
