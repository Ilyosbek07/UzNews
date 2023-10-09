from rest_framework import serializers

from apps.interview.models import Interview, InterviewTag, InterviewLike


class InterviewLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewLike
        fields = (
            "",
            "",
            "",
        )


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
            "updated_at"
        )


class InterviewDetailSerializer(serializers.ModelSerializer):
    tag = InterviewTagSerializer(many=True)
    related_interviews = serializers.SerializerMethodField()

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
            "related_interviews",
            "created_at"
        )
