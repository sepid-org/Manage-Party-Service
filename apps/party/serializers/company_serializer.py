from rest_framework import serializers

from apps.party.serializers.base_serializers import _PartySerializer
from apps.party.models import Company
from apps.site_appearance.serializers.header_data import HeaderDataSerializer
from apps.site_appearance.serializers.logo_serializer import LogoSerializer
from apps.site_appearance.serializers.og_metadata import OpenGraphMetadataSerializer


class CompanySerializer(_PartySerializer):
    logo = LogoSerializer()
    main_page_header_data = HeaderDataSerializer()
    main_page_og_metadata = OpenGraphMetadataSerializer()

    class Meta:
        model = Company
        fields = ['name', 'local_name', 'uuid', 'party_type',
                  'logo', 'main_page_header_data', 'main_page_og_metadata']
        read_only_fields = ['uuid', 'party_type',
                            'logo', 'main_page_header_data', 'main_page_og_metadata']
