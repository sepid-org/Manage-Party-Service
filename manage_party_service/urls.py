from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from manage_party_service.settings.base import get_environment_var, STATIC_ROOT, STATIC_URL, MEDIA_ROOT, MEDIA_URL
import sentry_sdk

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

# todo: sentry not working
if not settings.DEBUG and get_environment_var('SENTRY_DNS'):
    sentry_sdk.init(
        get_environment_var('SENTRY_DNS'),
        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        # We recommend adjusting this value in production.
        traces_sample_rate=1.0,
    )

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/party-manager/', include('apps.party.urls')),
    path('api/site-appearance/', include('apps.site_appearance.urls')),
]

urlpatterns += [path('api/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
                path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'), ]

urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
