import uuid
from django.db import models
from polymorphic.models import PolymorphicModel


class Party(PolymorphicModel):
    class PartyType(models.TextChoices):
        Individual = 'individual'
        Company = 'company'

    party_type = models.CharField(max_length=25, choices=PartyType.choices)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30, unique=True)
    local_name = models.CharField(max_length=50)


class Individual(Party):
    pass


class Company(Party):
    pass
