from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from apps.back_office.permissions import IsAuthor
from apps.back_office.serializers.photoreport import (
    PhotoReportListSerializer,
    PhotoReportDetailSerializer,
    PhotoReportSerializer,
)
from apps.photoreport.models import PhotoReport


class PhotoReportListAPIView(generics.ListAPIView):
    queryset = PhotoReport.objects.all()
    serializer_class = PhotoReportListSerializer
    permission_classes = (IsAuthenticated, IsAuthor)


class PhotoReportDetailAPIView(generics.RetrieveAPIView):
    queryset = PhotoReport.objects.all()
    serializer_class = PhotoReportDetailSerializer
    permission_classes = (IsAuthenticated, IsAuthor)


class PhotoReportCreateAPIView(generics.CreateAPIView):
    serializer_class = PhotoReportSerializer
    queryset = PhotoReport.objects.all()
    permission_classes = (IsAuthenticated, IsAuthor)


class PhotoReportUpdateAPIView(generics.UpdateAPIView):
    serializer_class = PhotoReportSerializer
    queryset = PhotoReport.objects.all()
    permission_classes = (IsAuthenticated, IsAuthor)


class PhotoReportDestroyAPIView(generics.DestroyAPIView):
    serializer_class = PhotoReportSerializer
    queryset = PhotoReport.objects.all()
    permission_classes = (IsAuthenticated, IsAuthor)
