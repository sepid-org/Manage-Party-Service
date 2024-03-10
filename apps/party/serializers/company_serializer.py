from apps.party.serializers.base_serializers import _PartySerializer
from apps.party.models import Company
from apps.party.serializers.logo_serializer import LogoSerializer
from apps.party.serializers.og_metadata import OpenGraphMetadataSerializer


class CompanySerializer(_PartySerializer):
    logo = LogoSerializer()
    og_metadata = OpenGraphMetadataSerializer()

    class Meta:
        model = Company
        fields = ['name', 'display_name', 'uuid', 'party_type', 'logo', 'og_metadata']
        read_only_fields = ['uuid', 'party_type', 'logo', 'og_metadata']
