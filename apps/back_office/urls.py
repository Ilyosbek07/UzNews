from django.urls import path

from apps.back_office.views import interview
from apps.back_office.views.news import NewsListAPIView, NewsDestroyAPIView, NewsCreateAPIView, NewsUpdateAPIView, \
    NewsRetrieveAPIView
from apps.back_office.views.photo_report import PhotoReportCreateAPIView, PhotoReportDetailAPIView, \
    PhotoReportUpdateAPIView, PhotoReportDestroyAPIView
from apps.back_office.views.podcast import PodcastDestroyAPIView, PodcastRetrieveAPIView, PodcastUpdateAPIView, \
    PodcastCreateAPIView, PodcastListAPIView

from apps.back_office.views.tag import (
    TagCreateAPIView,
    TagDestroyAPIView,
    TagUpdateAPIView,
)
from apps.back_office.views.profile import (
    UserProfileAPIView,
    ProfileUpdateView,
    UserUpdateView,
    ProfileListView,
    ProfileDestroyAPIView,
)
from apps.photoreport.views import PhotoReportListAPIView

urlpatterns = [
    # interview Urls
    path("interview/list/", interview.InterviewListAPIView.as_view(), name="back_interview_list"),
    path("interview/create/", interview.InterviewCreateAPIView.as_view(), name="back_interview_create"),
    path("interview/update/<int:pk>/", interview.InterviewUpdateAPIView.as_view(), name="back_interview_update"),
    path("interview/delete/<int:pk>/", interview.InterviewDestroyAPIView.as_view(), name="back_interview_delete"),
    path("interview/detail/<int:pk>/", interview.InterviewRetrieveAPIView.as_view(), name="back_interview_detail"),

    # tag Urls
    path("tag/create/", TagCreateAPIView.as_view(), name="back_tag_create"),
    path("tag/update/<int:pk>/", TagUpdateAPIView.as_view(), name="back_tag_update"),
    path("tag/delete/<int:pk>/", TagDestroyAPIView.as_view(), name="back_tag_delete"),

    # user Url
    path("user/edit/<int:pk>/", UserUpdateView.as_view(), name="back_user_edit"),

    # profile Urls
    path("profile/list/", ProfileListView.as_view(), name="back_profile_list"),
    path("profile/detail/", UserProfileAPIView.as_view(), name="back_profile_detail"),
    path("profile/edit/<int:pk>/", ProfileUpdateView.as_view(), name="back_profile_update"),
    path("profile/delete/<int:pk>", ProfileDestroyAPIView.as_view(), name="back_profile_delete"),

    # news Urls
    path("news/list/", NewsListAPIView.as_view(), name="back_news_list"),
    path("news/create/", NewsCreateAPIView.as_view(), name="back_news_create "),
    path("news/update/<int:pk>/", NewsUpdateAPIView.as_view(), name="back_news_update"),
    path("news/delete/<int:pk>/", NewsDestroyAPIView.as_view(), name="back_news_delete"),
    path("news/detail/<int:pk>/", NewsRetrieveAPIView.as_view(), name="back_news_detail"),

    # photo report Urls
    path("photo-report/list/", PhotoReportListAPIView.as_view(), name="back_photo_report_list"),
    path("photo-report/create/", PhotoReportCreateAPIView.as_view(), name="back_photo_report_create "),
    path("photo-report/update/<int:pk>/", PhotoReportUpdateAPIView.as_view(), name="back_photo_report_update"),
    path("photo-report/detail/<int:pk>/", PhotoReportDetailAPIView.as_view(), name="back_photo_report_detail"),
    path("photo-report/delete/<int:pk>/", PhotoReportDestroyAPIView.as_view(), name="back_photo_report_delete"),

    # podcast Urls
    path("podcast/list/", PodcastListAPIView.as_view(), name="back_podcast_list"),
    path("podcast/create/", PodcastCreateAPIView.as_view(), name="back_podcast_create "),
    path("podcast/update/<int:pk>/", PodcastUpdateAPIView.as_view(), name="back_podcast_update"),
    path("podcast/detail/<int:pk>/", PodcastRetrieveAPIView.as_view(), name="back_podcast_detail"),
    path("podcast/delete/<int:pk>/", PodcastDestroyAPIView.as_view(), name="back_podcast_delete"),
]
