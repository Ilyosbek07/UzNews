from rest_framework import serializers

from apps.common.choices import LikeStatusChoices
from apps.common.serializers import TagSerializer
from apps.interview.models import Interview, InterviewView


class InterviewSerializer(serializers.ModelSerializer):
    tag = TagSerializer(many=True)
    view_count = serializers.SerializerMethodField()

    class Meta:
        model = Interview
        fields = (
            "id",
            "title",
            "tag",
            "view_count",
            "date_time_in_word",
        )

    def get_view_count(self, obj):
        return InterviewView.objects.filter(interview=obj).count()


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
    view_count = serializers.SerializerMethodField()
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
            "view_count",
            "created_at",
        )

    def get_view_count(self, obj):
        return InterviewView.objects.filter(interview=obj).count()

    def get_likes_dislikes(self, obj):
        data = {
            "likes_count": obj.like_to_interview.filter(status=LikeStatusChoices.LIKED).count(),
            "dislikes_count": obj.like_to_interview.filter(status=LikeStatusChoices.DISLIKED).count(),
        }
        return data
