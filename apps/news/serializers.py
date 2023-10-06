from rest_framework import serializers
from .models import (
    NewsTag,
    NewsCategory,
    News,
    NewsLike,
    NewsComment,
    NewsCommentReport,
    NewsView,
    BreakingNews,
)


class NewsTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsTag
        fields = ("id", "name")


class NewsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsCategory
        fields = ("id", "name")


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = (
            "id",
            "cover",
            "tag",
            "category",
            "position",
            "status",
            "type",
            "title",
            "content",
            "created_at",
            "updated_at",
        )


class NewsLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsLike
        fields = ("id", "user", "news")


class NewsCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsComment
        fields = ("id", "user", "news", "text", "created_at", "updated_at")


class NewsCommentReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsCommentReport
        fields = ("id", "user", "comment")


class NewsViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsView
        fields = ("id", "user", "news")


class BreakingNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BreakingNews
        fields = ("id", "title", "news", "expire_time")
