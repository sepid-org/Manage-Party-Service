from django.conf import settings
from rest_framework import serializers
from apps.site_appearance.models import Banner


class BannerSerializer(serializers.ModelSerializer):
    desktop_image = serializers.SerializerMethodField()
    mobile_image = serializers.SerializerMethodField()

    class Meta:
        model = Banner
        fields = ['desktop_image', 'mobile_image', 'redirect_to']
        read_only_fields = ['desktop_image', 'mobile_image', 'redirect_to']

    def get_desktop_image(self, obj):
        return settings.SERVICE_DOMAIN + obj.desktop_image.url

    def get_mobile_image(self, obj):
        return settings.SERVICE_DOMAIN + obj.mobile_image.url
