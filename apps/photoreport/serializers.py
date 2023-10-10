from rest_framework import serializers

from apps.photoreport.models import Comment, GalleryImage, PhotoReport, Tag
from apps.users.models import User


class GalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = ("id", "image", "order")


class PrimePhotoReportSerializer(serializers.ModelSerializer):
    count_images = serializers.SerializerMethodField()
    gallery_image = GalleryImageSerializer(many=True)

    class Meta:
        model = PhotoReport
        fields = ("id", "slug", "title", "gallery_image", "count_images")

    def get_count_images(self, obj):
        return obj.gallery_image.count()


class PhotoReportListSerializer(serializers.ModelSerializer):
    count_images = serializers.SerializerMethodField()
    main_image = serializers.SerializerMethodField()

    class Meta:
        model = PhotoReport
        fields = ("id", "title", "slug", "count_images", "main_image")

    def get_count_images(self, obj):
        return obj.gallery_image.count()

    def get_main_image(self, obj):
        main_image = obj.gallery_image.filter(is_main=True).first()
        if main_image:
            return GalleryImageSerializer(instance=main_image).data
        return GalleryImageSerializer(instance=obj.gallery_image.first()).data


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("id", "name")


class PhotoReportDetailSerializer(serializers.ModelSerializer):
    gallery_image = GalleryImageSerializer(read_only=True, many=True)
    tag = TagSerializer(read_only=True, many=True)

    class Meta:
        model = PhotoReport
        fields = (
            "id",
            "title",
            "slug",
            "subtitle",
            "gallery_image",
            "desc",
            "views",
            "liked",
            "tag",
            "created_at",
        )


class CommentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name")


class CommentsListSerializer(serializers.ModelSerializer):
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
        serializer = CommentsListSerializer(instance=obj.comment.all(), many=True)
        return serializer.data


class CommentCreateSerializer(serializers.ModelSerializer):
    user = CommentUserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = (
            "text",
            "user",
            "image",
            "parent",
        )
