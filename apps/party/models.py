import uuid
from django.db import models
from polymorphic.models import PolymorphicModel


class Party(PolymorphicModel):
    class PartyType(models.TextChoices):
        Individual = 'individual'
        Company = 'company'

    party_type = models.CharField(max_length=25, choices=PartyType.choices)
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30, unique=True)
    local_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.local_name} | {self.name} | {self.party_type}'

class Individual(Party):
    pass


class Company(Party):
    pass


class PartyDomain(models.Model):
    party = models.ForeignKey(Party, on_delete=models.PROTECT)
    domain = models.CharField(max_length=100, unique=True)

    class Meta:
        unique_together = ('party', 'domain')
