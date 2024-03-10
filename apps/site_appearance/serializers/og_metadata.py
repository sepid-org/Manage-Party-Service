from django.conf import settings
from rest_framework import serializers
from apps.site_appearance.models import OpenGraphMetaData


def get_media_url():
    return settings.SERVICE_DOMAIN


class OpenGraphMetadataSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = OpenGraphMetaData
        fields = ['title', 'description', 'type', 'image', 'url']

    def get_image(self, obj):
        return get_media_url() + obj.image.url
