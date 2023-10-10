from rest_framework import serializers

from apps.interview.models import Interview, InterviewTag, InterviewView


class InterviewTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewTag
        fields = ("name",)


class InterviewSerializer(serializers.ModelSerializer):
    tag = InterviewTagSerializer(many=True)

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


class InterviewDetailSerializer(serializers.ModelSerializer):
    tag = InterviewTagSerializer(many=True)
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
