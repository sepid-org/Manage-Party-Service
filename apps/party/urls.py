from rest_framework.routers import DefaultRouter
from apps.party.views.party import PartyViewSet, get_party
from django.urls import path

router = DefaultRouter()

urlpatterns = [
    path('get-party/', get_party),
]

router.register(r'party', PartyViewSet)

urlpatterns += router.urls
