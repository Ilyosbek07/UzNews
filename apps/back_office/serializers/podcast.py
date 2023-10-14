from rest_framework import serializers

from apps.podcast.models import Podcast


class PodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields = (
            "title",
            "subtitle",
            "body",
            "status",
            "cover",
            "file",
            "tags",
            "author",
            "category"
        )


class PodcastListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields = (
            "title",
            "subtitle",
            "body",
            "status",
            "cover",
            "file",
            "tags",
            "author",
            "category"
        )

