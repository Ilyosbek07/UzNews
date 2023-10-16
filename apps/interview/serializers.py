from rest_framework import serializers

from apps.common.choices import LikeStatusChoices
from apps.common.serializers import TagSerializer
from apps.interview.models import Comment, Interview
from apps.users.models import User


class InterviewSerializer(serializers.ModelSerializer):
    tag = TagSerializer(many=True)

    class Meta:
        model = Interview
        fields = (
            "id",
            "title",
            "author",
            "slug",
            "status",
            "tag",
            "date_time_in_word",
        )


class InterviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = (
            "id",
            "title",
            "author",
            "subtitle",
            "status",
            "video_url",
            "tag",
        )


class InterviewDetailSerializer(serializers.ModelSerializer):
    tag = TagSerializer(many=True)

    class Meta:
        model = Interview
        fields = (
            "id",
            "author",
            "title",
            "subtitle",
            "status",
            "video_url",
            "tag",
            "date_time_in_word",
            "created_at",
        )


class InterviewCommentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name")


class InterviewCommentsListSerializer(serializers.ModelSerializer):
    user = InterviewCommentUserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = (
            "text",
            "user",
            "image",
            "parent",
        )


class InterviewCommentCreateSerializer(serializers.ModelSerializer):
    user = InterviewCommentUserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = (
            "text",
            "user",
            "image",
            "parent",
        )


class InterviewLikeDislikeSerializer(serializers.Serializer):
    type = serializers.ChoiceField(choices=("like", "dislike"))
