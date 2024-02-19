from rest_framework.routers import DefaultRouter
from apps.party.views.party import PartyViewSet, get_party_by_domain
from django.urls import path

router = DefaultRouter()

urlpatterns = [
    path('get_party_by_domain/', get_party_by_domain),
]

router.register(r'party', PartyViewSet)

urlpatterns += router.urls
