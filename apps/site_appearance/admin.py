from django.contrib import admin
from apps.site_appearance.models import Banner


class BannerAdmin(admin.ModelAdmin):
    model = Banner
    list_display = ['id', 'is_active']
    list_filter = ['is_active']


admin.site.register(Banner, BannerAdmin)
