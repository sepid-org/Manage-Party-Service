from django.contrib import admin
from apps.site_appearance.models import Logo, HeaderData, OpenGraphMetaData, Banner


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    model = Banner
    list_display = ['id', 'is_active']
    list_filter = ['is_active']


@admin.register(Logo)
class LogoAdmin(admin.ModelAdmin):
    model = Logo
    list_display = ['id']
    list_filter = []


@admin.register(HeaderData)
class HeaderDataAdmin(admin.ModelAdmin):
    model = HeaderData
    list_display = ['id']
    list_filter = []


@admin.register(OpenGraphMetaData)
class OpenGraphMetaDataAdmin(admin.ModelAdmin):
    model = OpenGraphMetaData
    list_display = ['id']
    list_filter = []
