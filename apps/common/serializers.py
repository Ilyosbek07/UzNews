from rest_framework import serializers
from apps.common.models import Advertising, SocialMedia


class AdvertisingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertising
        fields = ("id", "file", "type")


class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = ("id", "logo", "url", "number", "desc")
