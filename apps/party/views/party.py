from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from urllib.parse import urlparse

from apps.party.models import Party, PartyDomain
from apps.party.serializers.party_serializer import PartySerializer


class PartyViewSet(viewsets.ModelViewSet):
    # todo: it mustn't be allow to every one:
    permission_classes = [AllowAny]
    queryset = Party.objects.all()
    serializer_class = PartySerializer


@api_view(["GET"])
@permission_classes((AllowAny, ))
def get_party_by_domain(request):
    party_domain = urlparse(request.META['HTTP_ORIGIN']).netloc
    party_domain_object = PartyDomain.objects.get(domain=party_domain)
    serializer = PartySerializer(instance=party_domain_object.party)
    return Response(serializer.data)
