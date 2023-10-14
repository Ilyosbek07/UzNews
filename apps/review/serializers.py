from apps.common.models import ContentLike
from apps.users.models import User
from rest_framework import serializers

from apps.review.models import Review, Comment
from apps.photoreport.serializers import CommentUserSerializer, TagSerializer
from django.contrib.contenttypes.models import ContentType


class ReviewListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ("id", "category", "title", "cover")


class ReviewUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name")


class ReviewDetailSerializer(serializers.ModelSerializer):
    likes_dislikes = serializers.SerializerMethodField()
    author = ReviewUserSerializer()
    # tag = TagSerializer(many=True)

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
            "likes_dislikes",
            "view",
        )

    def get_likes_dislikes(self, obj):
        review = ContentType.objects.get_for_model(obj)
        data = {
            "like": ContentLike.objects.filter(content_type=review, status="l").count(),
            "dislike": ContentLike.objects.filter(
                content_type=review, status="d"
            ).count(),
        }
        return data


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


class ReviewCommentCreateSerializer(serializers.ModelSerializer):
    user = CommentUserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = (
            "text",
            "user",
            "image",
            "parent",
        )


class LikeDislikeSerializer(serializers.Serializer):
    type = serializers.ChoiceField(choices=("like", "dislike"))
