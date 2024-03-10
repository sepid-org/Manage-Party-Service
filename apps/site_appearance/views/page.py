import re
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from apps.site_appearance.models import Page
from apps.site_appearance.serializers.page import PageSerializer


@api_view(["GET"])
@permission_classes((AllowAny, ))
def get_page_metadata(request):
    party_uuid = request.GET.get('party')
    page_address = request.GET.get('page_address')
    print(party_uuid, "|||", page_address)
    pages = Page.objects.filter(party=party_uuid).order_by('-order', '-id')
    for page in pages:
        if re.search(page.address_pattern, page_address):
            return Response(PageSerializer(page).data)
    return Response()
