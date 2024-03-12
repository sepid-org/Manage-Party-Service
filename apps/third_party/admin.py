from django.contrib import admin
from apps.third_party.models import SMSService, SiteSupportService


@admin.register(SMSService)
class PageAdmin(admin.ModelAdmin):
    model = SMSService
    list_display = ['id', 'type', 'token', 'party']
    list_filter = ['party']


@admin.register(SiteSupportService)
class PageAdmin(admin.ModelAdmin):
    model = SiteSupportService
    list_display = ['id',  'type', 'token', 'party']
    list_filter = ['party']
