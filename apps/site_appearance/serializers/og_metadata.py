from rest_framework import serializers
from apps.site_appearance.models import OpenGraphMetaData
from apps.site_appearance.serializers.logo_serializer import get_media_url


class OpenGraphMetadataSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = OpenGraphMetaData
        fields = '__all__'

    def get_image(self, obj):
        return get_media_url() + obj.image.url
