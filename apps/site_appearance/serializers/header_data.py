from rest_framework import serializers
from apps.site_appearance.models import HeaderData


class HeaderDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = HeaderData
        fields = ['title', 'description', 'theme_color']
