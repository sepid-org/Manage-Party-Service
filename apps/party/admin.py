from django.contrib import admin
from apps.party.models import Individual, Company, OpenGraphMetaData, PartyDomain, Logo


@admin.register(Logo)
class LogoAdmin(admin.ModelAdmin):
    model = Logo
    list_display = ['id']
    list_filter = []


@admin.register(Individual)
class IndividualAdmin(admin.ModelAdmin):
    model = Individual
    list_display = ['name', 'display_name', 'uuid']
    list_filter = []


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    model = Company
    list_display = ['name', 'display_name', 'uuid']
    list_filter = []


@admin.register(PartyDomain)
class PartyDomainAdmin(admin.ModelAdmin):
    model = PartyDomain
    list_display = ['party', 'domain']
    list_filter = []


@admin.register(OpenGraphMetaData)
class OpenGraphMetaDataAdmin(admin.ModelAdmin):
    model = OpenGraphMetaData
    list_display = ['id']
    list_filter = []
