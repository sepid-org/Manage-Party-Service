from apps.party.serializers.base_serializers import _PartySerializer
from apps.party.models import Company
from apps.party.serializers.logo_serializer import LogoSerializer


class CompanySerializer(_PartySerializer):
    logo = LogoSerializer()

    class Meta:
        model = Company
        fields = ['name', 'display_name', 'uuid', 'party_type', 'logo']
        read_only_fields = ['uuid', 'party_type', 'logo']
