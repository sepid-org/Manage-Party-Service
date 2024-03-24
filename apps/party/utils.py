from django.conf import settings
from urllib.parse import urlparse
from apps.party.models import PartyDomain


def _get_media_url():
    return settings.SERVICE_DOMAIN


def _get_party_by_request(request):
    party_domain = urlparse(request.META['HTTP_ORIGIN']).netloc
    party_domain_object = PartyDomain.objects.get(domain=party_domain)
    return party_domain_object.party
