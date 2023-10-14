from apps.review.views import (
    ReviewListAPIView,
    ReviewDetailAPIView,
    RelatedReviewAPIView,
    CommentsListAPIView,
    ReviewCommentCreateAPIView,
    ReviewLikeDislikeAPIView,
    CommentLikeDislikeAPIView,
)
from django.urls import path

urlpatterns = [
    path("list/", ReviewListAPIView.as_view(), name="review_list"),
    path("<slug:slug>/detail/", ReviewDetailAPIView.as_view(), name="review_detail"),
    path("<slug:slug>/related/", RelatedReviewAPIView.as_view(), name="review_related"),
    path(
        "<slug:slug>/comments/list/",
        CommentsListAPIView.as_view(),
        name="photo_report_comments",
    ),
    path(
        "<slug:slug>/comment/create",
        ReviewCommentCreateAPIView.as_view(),
        name="comment_create",
    ),
    path(
        "<slug:slug>/like-dislike/",
        ReviewLikeDislikeAPIView.as_view(),
        name="review_like_dislike",
    ),
    path(
        "comment/<int:id>/like-dislike/",
        CommentLikeDislikeAPIView.as_view(),
        name="review_comment_like_dislike",
    ),
]
