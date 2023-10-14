from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics
from rest_framework.permissions import IsAdminUser

from apps.podcast.choices import PodcastStatusChoices
from apps.podcast.models import Podcast, Tag
from apps.podcast.serializers import (PodcastListSerializer,
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
    serializer_class = PodcastListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ("title",)
    filterset_fields = ("tags", "category")

    def get_queryset(self):
        return super().get_queryset().filter(status=PodcastStatusChoices.PUBLISHED).order_by("-created_at")[:10]
