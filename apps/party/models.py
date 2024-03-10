import uuid
from django.db import models
from polymorphic.models import PolymorphicModel


class Logo(models.Model):
    mobile_image = models.ImageField(upload_to='logos/')
    desktop_image = models.ImageField(upload_to='logos/')


class OpenGraphMetaData(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    type = models.CharField(max_length=100)
    image = models.ImageField(upload_to='og_images/')
    url = models.URLField(max_length=200)


class Party(PolymorphicModel):
    class PartyType(models.TextChoices):
        Individual = 'individual'
        Company = 'company'

    party_type = models.CharField(max_length=25, choices=PartyType.choices)
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    # the "name" is not necessary. it's useless until now:
    name = models.CharField(max_length=30, unique=True)
    display_name = models.CharField(max_length=20)

    logo = models.OneToOneField(Logo, on_delete=models.PROTECT, related_name='party')
    og_metadata = models.ForeignKey(OpenGraphMetaData, on_delete=models.PROTECT, related_name='party')

    def __str__(self):
        return f'{self.display_name} | {self.name} | {self.party_type}'


class Individual(Party):
    pass


class Company(Party):
    pass


class PartyDomain(models.Model):
    party = models.ForeignKey(Party, on_delete=models.PROTECT)
    domain = models.CharField(max_length=100, unique=True)

    class Meta:
        unique_together = ('party', 'domain')
