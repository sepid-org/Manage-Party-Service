from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from manage_party_service.settings.base import get_environment_var
import sentry_sdk
from django.views.static import serve

schema_view = get_schema_view(
    openapi.Info(
        title="Sepid Manage Party Servie",
        default_version='v3',
        description="APIs list of Sepid Manage Party Service",
    ),
    url=settings.SWAGGER_URL,
    public=True,
    permission_classes=(permissions.AllowAny,),
)

if not settings.DEBUG:
    sentry_sdk.init(
        get_environment_var('SENTRY_DNS'),
        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        # We recommend adjusting this value in production.
        traces_sample_rate=1.0,
    )

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/party/', include('apps.party.urls')),
    path('api/site-appearance/', include('apps.site_appearance.urls')),
]

urlpatterns += [path('api/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
                path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'), ]

urlpatterns += [
    re_path(r'^api/static/(?P<path>.*)$', serve,
            {'document_root': settings.STATIC_ROOT}),
    re_path(r'^api/media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT})
]
