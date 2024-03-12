from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from apps.third_party.models import ThirdParty
from apps.third_party.serializers.third_party import ThirdPartySerializer


@api_view(["GET"])
@permission_classes((AllowAny, ))
def get_third_party(request):
    party_uuid = request.GET.get('party')
    third_parties = ThirdParty.objects.filter(party=party_uuid)
    return Response(ThirdPartySerializer(third_parties, many=True).data)
