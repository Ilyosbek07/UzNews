from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers

from apps.common.models import ContentView
from apps.opinion.models import Category, Comment, Opinion, Tag
from apps.podcast.utils import time_difference_in_words
from apps.users.models import Profile


class OpinionTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("id", "name")


class OpinionCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name", "slug", "icon")


class OpinionProfileSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ("id", "name", "image", "role")

    def get_name(self, obj):
        user = obj.user
        return f"{user.last_name} {user.first_name}"


class OpinionCommentSerializer(serializers.ModelSerializer):
    profile = OpinionProfileSerializer()
    replies = serializers.SerializerMethodField()
    like_dislike_count = serializers.SerializerMethodField()
    is_mine = serializers.BooleanField()

    class Meta:
        model = Comment
        fields = ("id", "profile", "image", "text", "replies", "like_dislike_count", "is_mine")

    def get_replies(self, obj):
        return OpinionCommentSerializer(obj.replies.filter(is_active=True), many=True).data

    def get_like_dislike_count(self, obj):
        return obj.get_like_dislike_count()


class OpinionCommentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("id", "text", "image", "parent")


class OpinionCommentComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("id", "text")


class OpinionOpinionListSerializer(serializers.ModelSerializer):
    created_time_in_words = serializers.SerializerMethodField()
    category = OpinionCategorySerializer()
    view_count = serializers.SerializerMethodField()

    class Meta:
        model = Opinion
        fields = (
            "id",
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
        return obj.get_view_count()


class OpinionOpinionDetailSerializer(serializers.ModelSerializer):
    author = OpinionProfileSerializer()
    tags = OpinionTagSerializer(many=True)
    created_time_in_words = serializers.SerializerMethodField()
    category = OpinionCategorySerializer()
    view_count = serializers.SerializerMethodField()
    like_dislike_count = serializers.SerializerMethodField()

    class Meta:
        model = Opinion
        fields = (
            "id",
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
            "tags",
            "author",
            "category",
            "view_count",
            "like_dislike_count",
            "created_time_in_words",
        )

    def get_created_time_in_words(self, obj):
        return time_difference_in_words(obj.created_at)

    def get_view_count(self, obj):
        count = obj.get_view_count()
        user = self.context["user"]
        device_id = self.context["device_id"]
        ContentView.objects.get_or_create(
            content_type=ContentType.objects.get_for_model(Opinion), object_id=obj.id, user=user, device_id=device_id
        )
        return count

    def get_like_dislike_count(self, obj):
        return obj.get_like_dislike_count()
