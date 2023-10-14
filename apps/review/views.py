from apps.common.models import ContentLike
from apps.review.serializers import (
    ReviewListSerializers,
    ReviewDetailSerializer,
    RelatedReviewSerializer,
    ReviewCommentsListSerializer,
    ReviewCommentCreateSerializer,
    LikeDislikeSerializer,
)
from rest_framework import generics, status
from apps.review.models import Review, Comment, CommentLike
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from django.contrib.contenttypes.models import ContentType
from rest_framework.views import APIView


class ReviewListAPIView(generics.ListAPIView):
    serializer_class = ReviewListSerializers
    queryset = Review.objects.all().order_by("-created_at")


class ReviewDetailAPIView(generics.RetrieveAPIView):
    serializer_class = ReviewDetailSerializer
    queryset = Review.objects.all()
    lookup_field = "slug"


class RelatedReviewAPIView(generics.ListAPIView):
    serializer_class = RelatedReviewSerializer

    def get_queryset(self):
        slug = self.kwargs.get("slug")
        return Review.objects.exclude(slug=slug).order_by("-created_at")[:4]


class CommentsListAPIView(generics.ListAPIView):
    serializer_class = ReviewCommentsListSerializer

    def get_queryset(self):
        slug = self.kwargs.get("slug")
        return Comment.objects.filter(review__slug=slug, parent=None)


class ReviewCommentCreateAPIView(generics.CreateAPIView):
    serializer_class = ReviewCommentCreateSerializer
    parser_classes = (MultiPartParser,)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        review = Review.objects.get(slug=self.kwargs.get("slug"))
        text = serializer.validated_data.get("text")
        image = serializer.validated_data.get("image")
        parent = serializer.validated_data.get("parent")

        comment = Comment.objects.create(
            review=review, user=request.user, text=text, image=image, parent=parent
        )

        response_serializer = self.serializer_class(comment)

        return Response(response_serializer.data, status=status.HTTP_201_CREATED)


class ReviewLikeDislikeAPIView(generics.CreateAPIView):
    serializer_class = LikeDislikeSerializer

    def post(self, request, *args, **kwargs):
        slug = self.kwargs.get("slug")
        review = get_object_or_404(Review, slug=slug)
        type = request.data["type"]
        user = request.user
        if type == "like":
            like = ContentLike.objects.filter(
                content_type=ContentType.objects.get_for_model(review),
                object_id=review.id,
                user=user,
                status="d",
            )
            if like.exists():
                like.update(status="l")
                return Response(
                    {"message": "Review liked updated."}, status=status.HTTP_201_CREATED
                )
            try:
                ContentLike.objects.create_for_object(review, request.user, status="l")
                return Response(
                    {"message": "Review liked create successfully."},
                    status=status.HTTP_201_CREATED,
                )
            except:
                return Response({"message": "Review liked already have. "})

        elif type == "dislike":
            dislike = ContentLike.objects.filter(
                content_type=ContentType.objects.get_for_model(review),
                object_id=review.id,
                user=user,
                status="l",
            )
            if dislike.exists():
                dislike.update(status="d")
                return Response(
                    {"message": "Review disliked updated."},
                    status=status.HTTP_201_CREATED,
                )
            try:
                ContentLike.objects.create_for_object(review, request.user, status="d")
                return Response(
                    {"message": "Review disliked create successfully."},
                    status=status.HTTP_200_OK,
                )
            except:
                return Response({"message": "Review disliked already have. "})


class CommentLikeDislikeAPIView(APIView):
    def post(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, id=self.kwargs["id"])
        if request.user.is_authenticated:
            data = CommentLike.objects.filter(user=request.user, comment=comment)
            if data.exists():
                CommentLike.objects.filter(user=request.user, comment=comment).delete()
                comment.liked -= 1
                comment.save()
                return Response({"message": "successfully deleted. "})
            else:
                CommentLike.objects.create(user=request.user, comment=comment)
                comment.liked += 1
                return Response({"message": "successfully created. "})
        return Response({"message": "error"})
