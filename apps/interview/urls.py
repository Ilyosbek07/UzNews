from django.urls import path

from apps.interview.views import InterviewListAPIView, InterviewRetrieveAPIView, InterviewTagListAPIView, \
    RelatedInterviewsList, InterviewLikedView, InterviewDislikedView

urlpatterns = [
    path("tag/list/", InterviewTagListAPIView.as_view(), name="interview-list"),
    path("list/", InterviewListAPIView.as_view(), name="interview-list"),
    path("detail/<int:pk>/", InterviewRetrieveAPIView.as_view(), name="interview-detail"),
    path("related/<int:pk>/list/", RelatedInterviewsList.as_view(), name="interview-related"),
    path("liked/<int:pk>/", InterviewLikedView.as_view(), name="interview-liked"),
    path("disliked/<int:pk>/", InterviewDislikedView.as_view(), name="interview-disliked"),
]
