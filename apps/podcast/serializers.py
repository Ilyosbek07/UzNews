from django.contrib.contenttypes.models import ContentType
from django.db.models import BooleanField, Case, ExpressionWrapper, When
from rest_framework import serializers

from apps.common.choices import LikeStatusChoices
from apps.common.models import ContentLike, ContentView
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
    like_dislike_count = serializers.SerializerMethodField()
    is_mine = serializers.BooleanField()

    class Meta:
        model = Comment
        fields = ("id", "profile", "image", "text", "replies", "like_dislike_count", "is_mine")

    def get_replies(self, obj):
        return PodcastCommentSerializer(obj.replies.filter(is_active=True), many=True).data

    def get_like_dislike_count(self, obj):
        like_dislike = ContentLike.objects.filter(
            content_type=ContentType.objects.get_for_model(Comment), object_id=obj.id
        )
        like_count = like_dislike.filter(status=LikeStatusChoices.LIKED).count()
        dislike_count = like_dislike.filter(status=LikeStatusChoices.DISLIKED).count()
        return {"like": like_count, "dislike": dislike_count}


class PodcastCommentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("id", "text", "image", "parent")


class PodcastCommentComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("id", "text")


class PodcastPodcastListSerializer(serializers.ModelSerializer):
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
        return obj.get_view_count()


class PodcastPodcastDetailSerializer(serializers.ModelSerializer):
    author = PodcastProfileSerializer()
    tags = PodcastTagSerializer(many=True)
    comments = serializers.SerializerMethodField()
    created_time_in_words = serializers.SerializerMethodField()
    category = PodcastCategorySerializer()
    view_count = serializers.SerializerMethodField()
    like_dislike_count = serializers.SerializerMethodField()

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
            "like_dislike_count",
            "created_time_in_words",
        )

    def get_comments(self, obj):
        user = self.context["user"]
        try:
            profile = user.profile.first()
        except Exception as e:
            profile = None
        comments = obj.comments.filter(is_active=True).annotate(
            is_mine=ExpressionWrapper(
                Case(When(profile=profile, then=True), default=False), output_field=BooleanField()
            )
        )
        return PodcastCommentSerializer(comments, many=True).data

    def get_created_time_in_words(self, obj):
        return time_difference_in_words(obj.created_at)

    def get_view_count(self, obj):
        count = obj.get_view_count()
        user = self.context["user"]
        device_id = self.context["device_id"]
        ContentView.objects.get_or_create(
            content_type=ContentType.objects.get_for_model(Podcast), object_id=obj.id, user=user, device_id=device_id
        )
        return count

    def get_like_dislike_count(self, obj):
        like_dislike = ContentLike.objects.filter(
            content_type=ContentType.objects.get_for_model(Podcast), object_id=obj.id
        )
        like_count = like_dislike.filter(status=LikeStatusChoices.LIKED).count()
        dislike_count = like_dislike.filter(status=LikeStatusChoices.DISLIKED).count()
        return {"like": like_count, "dislike": dislike_count}
