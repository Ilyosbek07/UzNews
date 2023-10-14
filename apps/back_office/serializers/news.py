from rest_framework import serializers

from apps.news.models import News


class BackOfficeNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = (
            "cover",
            "tags",
            "category",
            "position",
            "status",
            "title",
            "is_verified",
            "style",
            "type",
            "author",
            "desc",
        )


class BackOfficeNewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = (
            "id",
            "cover",
            "tags",
            "category",
            "position",
            "status",
            "title",
            "is_verified",
            "style",
            "type",
            "author",
            "desc",
            "created_at",
        )
