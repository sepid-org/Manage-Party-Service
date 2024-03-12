from rest_framework import serializers
from apps.third_party.models import SMSService


class SMSServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = SMSService
        fields = ['token', 'party', 'type']
