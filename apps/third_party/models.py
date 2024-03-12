from django.db import models
from polymorphic.models import PolymorphicModel


class ThirdParty(PolymorphicModel):
    party = models.UUIDField()
    token = models.CharField(max_length=255, unique=True)


class SMSService(ThirdParty):
    class SMSServiceType(models.TextChoices):
        Kavenegar = 'Kavenegar'

    type = models.CharField(max_length=25, choices=SMSServiceType.choices)


class SiteSupportService(ThirdParty):
    class SiteSupportType(models.TextChoices):
        Goftino = 'Goftino'
        Crisp = 'Crisp'

    type = models.CharField(max_length=25, choices=SiteSupportType.choices)


# class VoiceCallService(ThirdParty):
#     # مثل کاوه‌نگار
#     pass


# class PaymentService(ThirdParty):
#     # مثل زرین‌پال
#     pass


# class ChatRoomService(ThirdParty):
#     # مثل قرار
#     pass

# initSentry()
# initGoogleAnalytics()
# initGoogleTagManager()
# initClarity()
