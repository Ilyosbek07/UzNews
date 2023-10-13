from apps.users.models import User
from rest_framework import serializers

from apps.review.models import Review, Comment
from apps.photoreport.serializers import CommentsListSerializer, CommentUserSerializer


class ReviewListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ("id", "category", "title", "cover")


class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = (
            "id",
            "title",
            "subtitle",
            "desc",
            "image",
            "tag",
            "author",
            "created_at",
            "liked",
            "view",
        )


class RelatedReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ("id", "category", "title", "cover")


class ReviewCommentsListSerializer(serializers.ModelSerializer):
    user = CommentUserSerializer(read_only=True)
    reply = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = (
            "id",
            "user",
            "image",
            "text",
            "reply",
            "liked",
            "created_at",
        )

    def get_reply(self, obj):
        serializer = ReviewCommentsListSerializer(instance=obj.replies.all(), many=True)
        return serializer.data
