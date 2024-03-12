from rest_framework import serializers
from apps.third_party.models import SiteSupportService


class SiteSupportServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = SiteSupportService
        fields = ['token', 'party', 'type']
