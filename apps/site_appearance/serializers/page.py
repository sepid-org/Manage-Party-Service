from rest_framework import serializers
from apps.site_appearance.models import Page
from apps.site_appearance.serializers.banner_serializer import BannerSerializer
from apps.site_appearance.serializers.header_data import HeaderDataSerializer
from apps.site_appearance.serializers.og_metadata import OpenGraphMetadataSerializer


class PageSerializer(serializers.ModelSerializer):
    header_data = HeaderDataSerializer()
    banners = serializers.SerializerMethodField()
    og_metadata = OpenGraphMetadataSerializer()

    def get_banners(self, obj):
        return BannerSerializer(obj.banners, many=True).data

    class Meta:
        model = Page
        fields = ['party', 'address_pattern',
                  'header_data', 'banners', 'og_metadata']
