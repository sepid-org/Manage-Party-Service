from apps.party.serializers.base_serializers import _PartySerializer
from apps.party.serializers.company_serializer import CompanySerializer
from apps.party.serializers.individual_serializer import IndividualSerializer
from rest_polymorphic.serializers import PolymorphicSerializer
from apps.party.models import Individual, Company


class PartySerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        Individual: IndividualSerializer,
        Company: CompanySerializer,
    }

    resource_type_field_name = 'party_type'
