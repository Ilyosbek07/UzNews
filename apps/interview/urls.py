from django.urls import path

from apps.interview.views import InterviewListAPIView, InterviewRetrieveAPIView, \
    RelatedInterviewsList, InterviewCreateAPIView

urlpatterns = [
    path("list/", InterviewListAPIView.as_view(), name="interview-list"),
    path("create/", InterviewCreateAPIView.as_view(), name="interview-create"),
    path("detail/<int:pk>/", InterviewRetrieveAPIView.as_view(), name="interview-detail"),
    path("<int:pk>/relatives/", RelatedInterviewsList.as_view(), name="interview-relative"),
]
