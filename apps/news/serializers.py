from rest_framework import serializers

from apps.common.choices import LikeStatusChoices
from apps.news.models import BreakingNews, News, NewsCategory
from apps.users.models import Profile


class NewsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsCategory
        fields = ("id", "name")


class NewsSerializer(serializers.ModelSerializer):
    category = NewsCategorySerializer()
    likes_dislikes = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()
    author = serializers.SerializerMethodField()

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
            "slug",
            "author",
            "desc",
            "likes_dislikes",
            "comments_count",
            "date_time_in_word",
            "view_count",
            "created_at",
            "updated_at",
        )

    def get_likes_dislikes(self, obj):
        data = {
            "likes_count": obj.news_like_to_news.filter(status=LikeStatusChoices.LIKED).count(),
            "dislikes_count": obj.news_like_to_news.filter(status=LikeStatusChoices.DISLIKED).count(),
        }
        return data

    def get_comments_count(self, obj):
        return obj.news_comment_to_news.count()

    def get_author(self, obj):
        from apps.users.serializers import UserProfileSerializer

        profile = Profile.objects.get(user=obj.author.id)
        return UserProfileSerializer(profile).data


class TimeLineNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ("id", "title", "created_at")


class BreakingNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BreakingNews
        fields = ("id", "title", "news", "expire_time")
