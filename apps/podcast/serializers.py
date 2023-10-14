from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers

from apps.common.models import ContentView
from apps.podcast.models import Category, Comment, Podcast, Tag
from apps.podcast.utils import time_difference_in_words
from apps.users.models import Profile


class PodcastTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("id", "name")


class PodcastCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name", "slug", "icon")


class PodcastProfileSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ("id", "name", "image", "role")

    def get_name(self, obj):
        user = obj.user
        return f"{user.last_name} {user.first_name}"


class PodcastCommentSerializer(serializers.ModelSerializer):
    profile = PodcastProfileSerializer()
    replies = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ("id", "profile", "image", "text", "replies")

    def get_replies(self, obj):
        return PodcastCommentSerializer(obj.replies.filter(is_active=True), many=True).data


class PodcastListSerializer(serializers.ModelSerializer):
    created_time_in_words = serializers.SerializerMethodField()
    category = PodcastCategorySerializer()
    view_count = serializers.SerializerMethodField()

    class Meta:
        model = Podcast
        fields = (
            "id",
            "cover",
            "title",
            "title_uz",
            "title_ru",
            "title_en",
            "category",
            "view_count",
            "created_time_in_words",
        )

    def get_created_time_in_words(self, obj):
        return time_difference_in_words(obj.created_at)

    def get_view_count(self, obj):
        return ContentView.objects.filter(
            content_type=ContentType.objects.get_for_model(Podcast), object_id=obj.id
        ).count()


class PodcastDetailSerializer(serializers.ModelSerializer):
    author = PodcastProfileSerializer()
    tags = PodcastTagSerializer(many=True)
    comments = serializers.SerializerMethodField()
    created_time_in_words = serializers.SerializerMethodField()
    category = PodcastCategorySerializer()
    view_count = serializers.SerializerMethodField()

    class Meta:
        model = Podcast
        fields = (
            "id",
            "cover",
            "title",
            "title_uz",
            "title_ru",
            "title_en",
            "slug",
            "subtitle",
            "subtitle_uz",
            "subtitle_ru",
            "subtitle_en",
            "body",
            "body_uz",
            "body_ru",
            "body_en",
            "file",
            "tags",
            "author",
            "category",
            "comments",
            "view_count",
            "created_time_in_words",
        )

    def get_comments(self, obj):
        return PodcastCommentSerializer(obj.comments.all(), many=True).data

    def get_created_time_in_words(self, obj):
        return time_difference_in_words(obj.created_at)

    def get_view_count(self, obj):
        count = ContentView.objects.filter(
            content_type=ContentType.objects.get_for_model(Podcast), object_id=obj.id
        ).count()
        user = self.context["user"]
        device_id = self.context["device_id"]
        ContentView.objects.get_or_create(
            content_type=ContentType.objects.get_for_model(Podcast), object_id=obj.id, user=user, device_id=device_id
        )
        return count
