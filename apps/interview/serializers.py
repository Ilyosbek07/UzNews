from rest_framework import serializers

from apps.common.serializers import TagSerializer
from apps.interview.models import Interview, InterviewView




class InterviewSerializer(serializers.ModelSerializer):
    tag = TagSerializer(many=True)

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
            "created_at",
            "updated_at",
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
    view_count = serializers.SerializerMethodField()

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
            "view_count",
            "created_at",
        )

    def get_view_count(self, obj):
        return InterviewView.objects.filter(interview=obj).count()
