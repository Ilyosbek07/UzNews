from rest_framework import serializers

from apps.interview.models import Interview, InterviewTag, InterviewLike


class InterviewLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewLike
        fields = (
            '',
            '',
            '',
        )

class InterviewTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewTag
        fields = ("name",)


class InterviewSerializer(serializers.ModelSerializer):
    tag = InterviewTagSerializer(many=True)

    class Meta:
        model = Interview
        fields = ("id", "tag", "subtitle", "video_url")
