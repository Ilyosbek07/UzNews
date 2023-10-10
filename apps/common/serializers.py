from rest_framework import serializers
from apps.common.models import Advertising, SocialMedia, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("name",)


class AdvertisingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertising
        fields = ("id", "file", "type")


class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = ("id", "logo", "url", "number", "desc")


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = None
        fields = ("text", "is_active", "image")
