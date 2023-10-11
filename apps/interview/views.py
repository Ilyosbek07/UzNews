from django.shortcuts import get_object_or_404
from rest_framework import filters, generics
from django_filters.rest_framework import DjangoFilterBackend
from apps.interview.models import Interview
from apps.interview.serializers import InterviewSerializer, InterviewDetailSerializer, InterviewCreateSerializer


class InterviewCreateAPIView(generics.CreateAPIView):
    queryset = Interview.objects.all()
    serializer_class = InterviewCreateSerializer


class InterviewListAPIView(generics.ListAPIView):
    queryset = Interview.objects.order_by("-created_at")
    serializer_class = InterviewSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ("title",)
    filterset_fields = ("tag", "status")


class InterviewRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Interview.objects.all()
    serializer_class = InterviewDetailSerializer

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     id = self.kwargs.get('pk')
    #     interview = get_object_or_404(queryset)
    #     if self.request.user.is_authenticated:
    #         InterviewView.objects.update_or_create(
    #             interview=interview,
    #             user=self.request.user,
    #         )
    #     elif self.request.headers.get("device-id", None):
    #         InterviewView.objects.update_or_create(
    #             interview=interview,
    #             device_id=self.request.headers.get("device-id", None),
    #         )
    #
    #     return queryset


class RelatedInterviewsList(generics.ListAPIView):
    serializer_class = InterviewSerializer
    def get_queryset(self):
        slug = self.kwargs.get('slug')
        return Interview.objects.exclude(slug=slug).order_by('-created_at')[:4]

# class
