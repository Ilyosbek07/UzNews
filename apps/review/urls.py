from apps.review.views import (
    ReviewListAPIView,
    ReviewDetailAPIView,
    RelatedReviewAPIView,
    CommentsListAPIView,
)
from django.urls import path

urlpatterns = [
    path("list/", ReviewListAPIView.as_view(), name="review_list"),
    path("<slug:slug>/", ReviewDetailAPIView.as_view(), name="review_detail"),
    path("<slug:slug>/related/", RelatedReviewAPIView.as_view(), name="review_related"),
    path(
        "<slug:slug>/comments/list/",
        CommentsListAPIView.as_view(),
        name="photo_report_comments",
    ),
]
