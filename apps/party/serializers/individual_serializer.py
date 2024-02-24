from apps.party.serializers.base_serializers import _PartySerializer
from apps.party.models import Individual


class IndividualSerializer(_PartySerializer):

    class Meta:
        model = Individual
        fields = ['name', 'display_name', 'uuid', 'party_type']
        read_only_fields = ['uuid', 'party_type']
