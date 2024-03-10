from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.response import Response

from apps.site_appearance.models import Banner
from apps.site_appearance.serializers.banner_serializer import BannerSerializer


class BannerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Banner.objects.filter(is_active=True)
    serializer_class = BannerSerializer

    @swagger_auto_schema(tags=['site-appearance'])
    def list(self, request, *args, **kwargs):
        banner_type = request.query_params.get('banner_type')
        banners = self.queryset.filter(banner_type=banner_type)
        return Response(data=self.serializer_class(banners, context={'request': request}, many=True).data, status=status.HTTP_200_OK)
