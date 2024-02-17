from apps.party.serializers.base_serializers import _PartySerializer
from apps.party.models import Company


class CompanySerializer(_PartySerializer):

    class Meta:
        model = Company
        fields = ['name', 'local_name', 'uuid', 'party_type']
        read_only_fields = ['uuid', 'party_type']
