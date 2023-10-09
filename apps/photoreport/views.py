from rest_framework import generics

from apps.photoreport.models import Comment, PhotoReport
from apps.photoreport.serializers import (CommentsListSerializer,
                                          PhotoReportDetailSerializer,
                                          PhotoReportListSerializer)


class PhotoReportListAPIView(generics.ListAPIView):
    queryset = PhotoReport.objects.all()
    serializer_class = PhotoReportListSerializer


class PhotoReportDetailAPIView(generics.RetrieveAPIView):
    queryset = PhotoReport.objects.all()
    serializer_class = PhotoReportDetailSerializer
    lookup_field = "slug"


class CommentsListAPIView(generics.ListAPIView):
    serializer_class = CommentsListSerializer

    def get_queryset(self):
        slug = self.kwargs.get("slug")
        return Comment.objects.filter(photo_report__slug=slug, parent=None)
