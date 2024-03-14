from rest_framework import serializers
from apps.site_appearance.models import Appbar


class AppbarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appbar
        fields = ['body']
