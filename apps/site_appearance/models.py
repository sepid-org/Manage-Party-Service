from django.db import models


# WHOLE SITE:

class Logo(models.Model):
    mobile_image = models.ImageField(upload_to='logos/')
    desktop_image = models.ImageField(upload_to='logos/')


class HeaderData(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    theme_color = models.CharField(max_length=10, default='#ffffff')
    icon = models.ImageField(upload_to='party_icons/', null=True)

# PAGES:


class OpenGraphMetaData(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    type = models.CharField(max_length=100)
    image = models.ImageField(upload_to='og_images/')
    url = models.URLField(max_length=200)


class Banner(models.Model):
    mobile_image = models.ImageField(upload_to='banners/')
    desktop_image = models.ImageField(upload_to='banners/')
    is_active = models.BooleanField(default=False)
    redirect_to = models.URLField()
