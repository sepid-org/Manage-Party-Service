from django.contrib import admin
from apps.site_appearance.models import HeaderData, Banner, Page


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    model = Page
    list_display = ['id', 'address_pattern']
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
