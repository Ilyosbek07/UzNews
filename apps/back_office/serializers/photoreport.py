from rest_framework import serializers

from apps.photoreport.models import PhotoReport
from apps.photoreport.serializers import GalleryImageSerializer


class PhotoReportListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoReport
        fields = ("id", "title", "slug", "status")


class PhotoReportDetailSerializer(serializers.ModelSerializer):
    gallery_image = GalleryImageSerializer(read_only=True, many=True)

    class Meta:
        model = PhotoReport
        fields = (
            "id",
            "title",
            "slug",
            "subtitle",
            "gallery_image",
            "desc",
            "created_at",
        )


class PhotoReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoReport
        fields = (
            "title",
            "subtitle",
            "status",
            "desc",
        )
