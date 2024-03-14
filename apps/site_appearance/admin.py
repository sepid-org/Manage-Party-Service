from django.contrib import admin
from apps.site_appearance.models import HeaderData, Banner, Page, OpenGraphMetaData, Appbar


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    model = Page
    list_display = ['name', 'address_pattern', 'party']
    list_filter = ['party']


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    model = Banner
    list_display = ['id', 'is_active']
    list_filter = ['is_active']


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


@admin.register(Appbar)
class AppbarAdmin(admin.ModelAdmin):
    model = Appbar
    list_display = ['id']
    list_filter = []
