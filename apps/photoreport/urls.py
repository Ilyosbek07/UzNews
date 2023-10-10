from django.urls import path

from apps.photoreport.views import (CommentCreateAPIView, CommentsListAPIView,
                                    CreateDislikeCommentAPIView,
                                    CreateLikeCommentAPIView,
                                    PhotoReportDetailAPIView,
                                    PhotoReportDislikeAPIView,
                                    PhotoReportLikeAPIView,
                                    PhotoReportListAPIView,
                                    PrimePhotoReportAPIView)

urlpatterns = [
    path("prime/", PrimePhotoReportAPIView.as_view(), name="prime_photo_report"),
    path("list/", PhotoReportListAPIView.as_view(), name="photo_report_list"),
    path(
        "detail/<slug:slug>/",
        PhotoReportDetailAPIView.as_view(),
        name="photo_report_detail",
    ),
    path("<slug:slug>/like", PhotoReportLikeAPIView.as_view(), name="photo_report_like"),
    path("<slug:slug>/dislike", PhotoReportDislikeAPIView.as_view(), name="photo_report_dislike"),
    path(
        "<slug:slug>/comments/list/",
        CommentsListAPIView.as_view(),
        name="photo_report_comments",
    ),
    path("<slug:slug>/comment/create", CommentCreateAPIView.as_view(), name="comment_create"),
    path("comment/<int:id>/like", CreateLikeCommentAPIView.as_view(), name="create_like"),
    path("comment/<int:id>/dislike", CreateDislikeCommentAPIView.as_view(), name="create_dislike"),
]
