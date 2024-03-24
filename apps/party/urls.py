from rest_framework.routers import DefaultRouter
from apps.party.views.party import PartyViewSet, get_party
from apps.party.views.open_graph import OpenGraphMetaDataViewSet, get_open_graph_metadata
from django.urls import path

router = DefaultRouter()

urlpatterns = [
    path('get-party/', get_party),
    path('get-og_metadata/', get_open_graph_metadata),
]

router.register(r'party', PartyViewSet)
router.register(r'og_metadata', OpenGraphMetaDataViewSet)

urlpatterns += router.urls
