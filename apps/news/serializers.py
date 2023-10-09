from rest_framework import serializers

from .models import (BreakingNews, News, NewsCategory, NewsComment,
                     NewsCommentReport, NewsLike, NewsTag, NewsView)


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
            "title",
            "style",
            "slug",
            "author",
            "desc",
            "date_time_in_word",
            "view_count",
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
