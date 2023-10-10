from django.urls import path

from apps.interview.views import InterviewListAPIView, InterviewRetrieveAPIView, InterviewTagListAPIView

urlpatterns = [
    path("tag/list/", InterviewTagListAPIView.as_view(), name="interview-list"),
    path("list/", InterviewListAPIView.as_view(), name="interview-list"),
    path("detail/<int:pk>/", InterviewRetrieveAPIView.as_view(), name="interview-detail"),
]
