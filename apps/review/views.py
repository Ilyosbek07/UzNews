from apps.review.serializers import (
    ReviewListSerializers,
    ReviewDetailSerializer,
    RelatedReviewSerializer,
    ReviewCommentsListSerializer,
)
from rest_framework import generics
from apps.review.models import Review, Comment


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
