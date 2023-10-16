from django.urls import path

from apps.interview.views import (InterviewCommentCreateAPIView,
                                  InterviewCommentLikeDislikeAPIView,
                                  InterviewCommentsListAPIView,
                                  InterviewLikeDislikeAPIView,
                                  InterviewListAPIView,
                                  InterviewRetrieveAPIView,
                                  RelatedInterviewsList)

urlpatterns = [
    path("list/", InterviewListAPIView.as_view(), name="interview-list"),
    path("detail/<int:pk>/", InterviewRetrieveAPIView.as_view(), name="interview-detail"),
    path("related/interview/<slug:slug>/list/", RelatedInterviewsList.as_view(), name="related_interviews"),
    path(
        "<slug:slug>/comments/list/",
        InterviewCommentsListAPIView.as_view(),
        name="interview_comments",
    ),
    path(
        "<slug:slug>/comment/create",
        InterviewCommentCreateAPIView.as_view(),
        name="interview_comment_create",
    ),
    path(
        "<slug:slug>/like-dislike/",
        InterviewLikeDislikeAPIView.as_view(),
        name="interview_like_dislike",
    ),
    path(
        "comment/<int:id>/like-dislike/",
        InterviewCommentLikeDislikeAPIView.as_view(),
        name="review_comment_like_dislike",
    ),
]
