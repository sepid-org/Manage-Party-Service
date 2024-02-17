from rest_framework import permissions, viewsets
from apps.party.models import Party
from apps.party.serializers.party_serializer import PartySerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions


class PartyViewSet(viewsets.ModelViewSet):
    # todo: it mustn't be allow to every one:
    permission_classes = [permissions.AllowAny]
    queryset = Party.objects.all()
    serializer_class = PartySerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = PartySerializer(instance=instance)
        return Response(serializer.data)
