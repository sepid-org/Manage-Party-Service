from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from apps.party.models import OpenGraphMetaData
from apps.party.serializers.og_metadata import OpenGraphMetadataSerializer
from apps.party.utils import _get_party_by_request


class OpenGraphMetaDataViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = OpenGraphMetaData.objects.all()
    serializer_class = OpenGraphMetadataSerializer


@api_view(["GET"])
@permission_classes((AllowAny, ))
def get_open_graph_metadata(request):
    party = _get_party_by_request(request)
    serializer = OpenGraphMetadataSerializer(instance=party.og_metadata)
    return Response(serializer.data)
