from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated

from apps.back_office.permissions import IsAuthor
from apps.back_office.serializers.podcast import PodcastListSerializer, PodcastSerializer
from apps.podcast.models import Podcast


class PodcastListAPIView(generics.ListAPIView):
    serializer_class = PodcastListSerializer
    queryset = Podcast.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ("title",)
    filterset_fields = ("status",)
    permission_classes = (IsAuthenticated, IsAuthor)


class PodcastRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = PodcastSerializer
    queryset = Podcast.objects.all()
    permission_classes = (IsAuthenticated, IsAuthor)


class PodcastCreateAPIView(generics.CreateAPIView):
    serializer_class = PodcastSerializer
    queryset = Podcast.objects.all()
    parser_classes = (MultiPartParser,)
    permission_classes = (IsAuthenticated, IsAuthor)


class PodcastUpdateAPIView(generics.UpdateAPIView):
    serializer_class = PodcastSerializer
    queryset = Podcast.objects.all()
    parser_classes = (MultiPartParser,)
    permission_classes = (IsAuthenticated, IsAuthor)


class PodcastDestroyAPIView(generics.DestroyAPIView):
    serializer_class = PodcastSerializer
    queryset = Podcast.objects.all()
    permission_classes = (IsAuthenticated, IsAuthor)
