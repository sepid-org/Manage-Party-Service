from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from apps.party.models import Party
from apps.party.serializers.party_serializer import PartySerializer
from apps.party.utils import _get_party_by_request


class PartyViewSet(viewsets.ModelViewSet):
    # todo: it mustn't be allow to every one:
    permission_classes = [AllowAny]
    queryset = Party.objects.all()
    serializer_class = PartySerializer


@api_view(["GET"])
@permission_classes((AllowAny, ))
def get_party(request):
    party = _get_party_by_request(request)
    serializer = PartySerializer(instance=party)
    return Response(serializer.data)
