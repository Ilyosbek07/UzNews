from rest_framework import serializers

from apps.common.choices import LikeStatusChoices
from apps.common.serializers import TagSerializer
from apps.interview.models import Interview


class InterviewSerializer(serializers.ModelSerializer):
    tag = TagSerializer(many=True)

    class Meta:
        model = Interview
        fields = (
            "id",
            "title",
            "slug",
            "tag",
            "date_time_in_word",
        )


class InterviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = (
            "title",
            "subtitle",
            "status",
            "video_url",
            "tag",
        )


class InterviewDetailSerializer(serializers.ModelSerializer):
    tag = TagSerializer(many=True)
    likes_dislikes = serializers.SerializerMethodField()

    class Meta:
        model = Interview
        fields = (
            "id",
            "title",
            "subtitle",
            "status",
            "video_url",
            "tag",
            "date_time_in_word",
            "likes_dislikes",
            "created_at",
        )

    def get_likes_dislikes(self, obj):
        data = {
            "likes_count": obj.like_to_interview.filter(status=LikeStatusChoices.LIKED).count(),
            "dislikes_count": obj.like_to_interview.filter(status=LikeStatusChoices.DISLIKED).count(),
        }
        return data
