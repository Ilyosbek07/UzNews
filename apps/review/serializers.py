from rest_framework import serializers

from apps.review.models import Review


class ReviewListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ("id", "category", "title", "cover")
