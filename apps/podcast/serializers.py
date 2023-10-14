from rest_framework import serializers

from apps.podcast.models import (Category, Comment, CommentComplaint, Podcast,
                                 Tag)
from apps.podcast.utils import time_difference_in_words
from apps.users.models import Profile


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("id", "name")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name", "slug", "icon")


class ProfileSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ("id", "name", "image", "role")

    def get_name(self, obj):
        user = obj.user
        return f"{user.last_name} {user.first_name}"


class CommentSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    replies = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ("id", "profile", "image", "text", "replies")

    def get_replies(self, obj):
        return CommentSerializer(obj.replies.filter(is_active=True), many=True).data


class PodcastListSerializer(serializers.ModelSerializer):
    created_time_in_words = serializers.SerializerMethodField()
    category = CategorySerializer()

    class Meta:
        model = Podcast
        fields = ("id", "cover", "created_time_in_words", "title", "title_uz", "title_ru", "title_en", "category")

    def get_created_time_in_words(self, obj):
        return time_difference_in_words(obj.created_at)
