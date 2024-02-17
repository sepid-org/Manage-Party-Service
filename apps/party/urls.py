from rest_framework.routers import DefaultRouter
from apps.party.views.party import PartyViewSet

router = DefaultRouter()

urlpatterns = []

router.register(r'party', PartyViewSet)

urlpatterns += router.urls
