from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics

from apps.interview.models import Interview
from apps.interview.serializers import (InterviewCreateSerializer,
                                        InterviewDetailSerializer,
                                        InterviewSerializer)


class InterviewListAPIView(generics.ListAPIView):
    queryset = Interview.objects.order_by("-created_at")
    serializer_class = InterviewSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ("title",)
    filterset_fields = ("tag", "status")


class InterviewCreateAPIView(generics.CreateAPIView):
    queryset = Interview.objects.all()
    serializer_class = InterviewCreateSerializer


class InterviewDestroyAPIView(generics.DestroyAPIView):
    queryset = Interview.objects.all()
    serializer_class = InterviewCreateSerializer


class InterviewUpdateAPIView(generics.UpdateAPIView):
    queryset = Interview.objects.all()
    serializer_class = InterviewCreateSerializer


class InterviewRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Interview.objects.all()
    serializer_class = InterviewDetailSerializer


class RelatedInterviewsList(generics.ListAPIView):
    serializer_class = InterviewSerializer

    def get_queryset(self):
        slug = self.kwargs.get("slug")
        return Interview.objects.exclude(slug=slug).order_by("-created_at")[:4]
