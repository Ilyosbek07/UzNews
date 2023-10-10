from django.shortcuts import get_object_or_404
from rest_framework import filters, generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from apps.interview.models import Interview, InterviewView
from apps.interview.serializers import (InterviewSerializer,
                                         InterviewDetailSerializer, InterviewCreateSerializer)


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

    def get_queryset(self):
        queryset = super().get_queryset()
        id = self.kwargs.get('pk')
        interview = get_object_or_404(queryset, id=id)
        if self.request.user.is_authenticated:
            InterviewView.objects.update_or_create(
                interview=interview,
                user=self.request.user,
            )
        elif self.request.headers.get("device-id", None):
            InterviewView.objects.update_or_create(
                interview=interview,
                device_id=self.request.headers.get("device-id", None),
            )

        return queryset


class RelatedInterviewsList(generics.ListAPIView):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer

    def get(self, request, pk=None, *args, **kwargs):
        obj = get_object_or_404(self.queryset, id=pk)

        related_products = self.queryset.filter(tag__in=obj.tag.all()).exclude(id=pk).order_by('?')[:5]

        serializer = self.serializer_class(instance=related_products, many=True)
        return Response(serializer.data)
