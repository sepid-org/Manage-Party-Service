from rest_framework import serializers
from apps.third_party.models import SiteSupportService, SMSService
from apps.third_party.serializers.site_support_service import SiteSupportServiceSerializer
from apps.third_party.serializers.sms_service import SMSServiceSerializer
from rest_polymorphic.serializers import PolymorphicSerializer


class ThirdPartySerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        SiteSupportService: SiteSupportServiceSerializer,
        SMSService: SMSServiceSerializer,
    }

    resource_type_field_name = 'third_party_type'
