from django.urls import path

from apps.photoreport.views import (CommentsListAPIView,
                                    PhotoReportDetailAPIView,
                                    PhotoReportListAPIView)

urlpatterns = [
    path("list/", PhotoReportListAPIView.as_view(), name="photo_report_list"),
    path(
        "detail/<slug:slug>/",
        PhotoReportDetailAPIView.as_view(),
        name="photo_report_detail",
    ),
    path(
        "<slug:slug>/comments/list/",
        CommentsListAPIView.as_view(),
        name="photo_report_comments",
    ),
]
