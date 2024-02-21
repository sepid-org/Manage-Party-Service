from rest_framework import serializers
from apps.site_appearance.models import HeaderData
from apps.site_appearance.serializers.logo_serializer import get_media_url


class HeaderDataSerializer(serializers.ModelSerializer):
    icon = serializers.SerializerMethodField()

    class Meta:
        model = HeaderData
        fields = '__all__'

    def get_icon(self, obj):
        if obj.icon:
            return get_media_url() + obj.icon.url
        return None
