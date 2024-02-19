from django.contrib import admin
from apps.party.models import Individual, Company, PartyDomain


@admin.register(Individual)
class IndividualAdmin(admin.ModelAdmin):
    model = Individual
    list_display = ['name', 'local_name', 'uuid']
    list_filter = []


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    model = Company
    list_display = ['name', 'local_name', 'uuid']
    list_filter = []


@admin.register(PartyDomain)
class PartyDomainAdmin(admin.ModelAdmin):
    model = PartyDomain
    list_display = ['party', 'domain']
    list_filter = []
