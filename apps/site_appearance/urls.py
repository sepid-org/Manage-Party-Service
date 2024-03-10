from rest_framework.routers import DefaultRouter
from django.urls import path
from apps.site_appearance.views.banner import BannerViewSet
from apps.site_appearance.views.page import get_page_metadata

router = DefaultRouter()

urlpatterns = [
    path('get-page-metadata/', get_page_metadata),
]

router.register(r'banner', BannerViewSet)

urlpatterns += router.urls
