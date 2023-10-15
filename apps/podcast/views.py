import uuid

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics
from rest_framework.permissions import IsAdminUser

from apps.podcast.choices import PodcastStatusChoices
from apps.podcast.models import Podcast, Tag
from apps.podcast.serializers import (PodcastPodcastDetailSerializer,
                                      PodcastPodcastListSerializer,
                                      PodcastTagSerializer)


class PodcastTagListView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = PodcastTagSerializer


class PodcastTagCreateView(generics.CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = PodcastTagSerializer
    permission_classes = [IsAdminUser]


class NewPodcastsView(generics.ListAPIView):
    queryset = Podcast.objects.all()
    serializer_class = PodcastPodcastListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ("title",)
    filterset_fields = ("tags", "category")

    def get_queryset(self):
        return super().get_queryset().filter(status=PodcastStatusChoices.PUBLISHED).order_by("-created_at")[:10]


class PodcastDetailView(generics.RetrieveAPIView):
    queryset = Podcast.objects.filter(status=PodcastStatusChoices.PUBLISHED)
    serializer_class = PodcastPodcastDetailSerializer
    lookup_field = "slug"

    def get_serializer_context(self):
        context = super().get_serializer_context()
        user = self.request.user
        if not user.is_authenticated:
            user = None
        device_id = self.request.headers.get("HTTP_X_DEVICE", None)
        if user is None and device_id is None:
            device_id = uuid.uuid4()
        context.update({"user": user, "device_id": device_id})
        return context
