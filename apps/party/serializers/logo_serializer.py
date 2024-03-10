from django.conf import settings
from rest_framework import serializers
from apps.party.models import Logo


def get_media_url():
    return settings.SERVICE_DOMAIN


class LogoSerializer(serializers.ModelSerializer):
    desktop_image = serializers.SerializerMethodField()
    mobile_image = serializers.SerializerMethodField()

    class Meta:
        model = Logo
        fields = ['desktop_image', 'mobile_image']

    def get_desktop_image(self, obj):
        return get_media_url() + obj.desktop_image.url

    def get_mobile_image(self, obj):
        return get_media_url() + obj.mobile_image.url
