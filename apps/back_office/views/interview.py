from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated

from apps.back_office.permissions import IsAuthor, IsModerator
from apps.interview.models import Interview
from apps.interview.serializers import InterviewCreateSerializer, InterviewSerializer, InterviewDetailSerializer


class InterviewListAPIView(generics.ListAPIView):
    queryset = Interview.objects.order_by("-created_at")
    serializer_class = InterviewSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ("title",)
    filterset_fields = ("tag", "status")
    permission_classes = (IsAuthenticated, IsAuthor)


class InterviewCreateAPIView(generics.CreateAPIView):
    queryset = Interview.objects.all()
    serializer_class = InterviewCreateSerializer
    permission_classes = (IsAuthenticated, IsAuthor)


class InterviewDestroyAPIView(generics.DestroyAPIView):
    queryset = Interview.objects.all()
    serializer_class = InterviewCreateSerializer
    permission_classes = (IsAuthenticated, IsAuthor)


class InterviewUpdateAPIView(generics.UpdateAPIView):
    queryset = Interview.objects.all()
    serializer_class = InterviewCreateSerializer
    permission_classes = (IsAuthenticated, IsAuthor)


class InterviewRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Interview.objects.all()
    serializer_class = InterviewDetailSerializer
    permission_classes = (IsAuthenticated, IsAuthor)
