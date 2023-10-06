from django.urls import path

from apps.interview.views import (
    InterviewListAPIView,
    InterviewTagListAPIView,
    InterviewRetrieveAPIView,
)

urlpatterns = [
    path("tag/list/", InterviewTagListAPIView.as_view(), name="interview-list"),
    path("list/", InterviewListAPIView.as_view(), name="interview-list"),
    path("detail/", InterviewRetrieveAPIView.as_view(), name="interview-detail"),
]
