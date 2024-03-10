from django.db import models


class HeaderData(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    theme_color = models.CharField(max_length=10, default='#ffffff')
    icon = models.ImageField(upload_to='party_icons/', null=True)


class OpenGraphMetaData(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    type = models.CharField(max_length=100)
    image = models.ImageField(upload_to='og_images/')
    url = models.URLField(max_length=200)


class Page(models.Model):
    party = models.UUIDField()
    address_pattern = models.CharField(max_length=100)
    header_data = models.OneToOneField(
        HeaderData, on_delete=models.PROTECT, related_name='page')
    og_metadata = models.OneToOneField(
        OpenGraphMetaData, on_delete=models.PROTECT, related_name='page', null=True, blank=True)
    order = models.IntegerField(default=0)


class Banner(models.Model):
    page = models.ForeignKey(Page, on_delete=models.PROTECT, related_name='banners')
    mobile_image = models.ImageField(upload_to='banners/')
    desktop_image = models.ImageField(upload_to='banners/')
    is_active = models.BooleanField(default=False)
    redirect_to = models.URLField()
