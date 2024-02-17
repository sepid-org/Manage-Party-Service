from django.db import models


class Banner(models.Model):
    desktop_image = models.ImageField(upload_to='banners/')
    mobile_image = models.ImageField(upload_to='banners/')
    is_active = models.BooleanField(default=False)
    redirect_to = models.URLField()


class Logo(models.Model):
    mobile_image = models.ImageField(upload_to='logos/')
    desktop_image = models.ImageField(upload_to='logos/')


# گفتینو - قالب رنگی - منوی بالا
