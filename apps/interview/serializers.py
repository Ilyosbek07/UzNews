from rest_framework import serializers

from apps.interview.models import Interview, InterviewTag


class InterviewTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewTag
        fields = ('name',)


class InterviewSerializer(serializers.ModelSerializer):
    tag = InterviewTagSerializer(many=True)

    class Meta:
        model = Interview
        fields = (
            'id',
            'tag',
            'subtitle',
            'video_url'
        )
