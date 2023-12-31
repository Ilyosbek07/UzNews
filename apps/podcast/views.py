import uuid

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.podcast.choices import PodcastStatusChoices
from apps.podcast.models import Comment, CommentComplaint, Podcast, Tag
from apps.podcast.serializers import (PodcastCommentComplaintSerializer,
                                      PodcastCommentDetailSerializer,
                                      PodcastPodcastDetailSerializer,
                                      PodcastPodcastListSerializer,
                                      PodcastTagSerializer)
from apps.podcast.utils import perform_object_liked_disliked


class PodcastTagListView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = PodcastTagSerializer


class NewPodcastsView(generics.ListAPIView):
    queryset = Podcast.objects.all()
    serializer_class = PodcastPodcastListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ("title",)
    filterset_fields = ("tags", "category")

    def get_queryset(self):
        return super().get_queryset().filter(status=PodcastStatusChoices.PUBLISHED).order_by("-created_at")[:10]


class MostViewedPodcastsView(generics.ListAPIView):
    queryset = Podcast.objects.all()
    serializer_class = PodcastPodcastListSerializer

    def get_queryset(self):
        queryset = super().get_queryset().filter(status=PodcastStatusChoices.PUBLISHED)
        return sorted(queryset, key=lambda obj: obj.get_view_count(), reverse=True)[:10]


class MostCommentedPodcastsView(generics.ListAPIView):
    queryset = Podcast.objects.all()
    serializer_class = PodcastPodcastListSerializer

    def get_queryset(self):
        queryset = super().get_queryset().filter(status=PodcastStatusChoices.PUBLISHED)
        return sorted(queryset, key=lambda obj: obj.comments.count(), reverse=True)[:10]


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


class PodcastLikedView(generics.RetrieveAPIView):
    queryset = Podcast.objects.filter(status=PodcastStatusChoices.PUBLISHED)
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, pk, *args, **kwargs):
        user = self.request.user
        return Response(
            perform_object_liked_disliked(
                object_id=pk, ObjectModel=Podcast, queryset=self.queryset, user=user, liked=True
            )
        )


class PodcastDislikedView(generics.RetrieveAPIView):
    queryset = Podcast.objects.filter(status=PodcastStatusChoices.PUBLISHED)
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, pk, *args, **kwargs):
        user = self.request.user
        return Response(
            perform_object_liked_disliked(
                object_id=pk, ObjectModel=Podcast, queryset=self.queryset, user=user, liked=False
            )
        )


class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = PodcastCommentDetailSerializer

    def post(self, request, podcast_id, *args, **kwargs):
        try:
            podcast = Podcast.objects.get(pk=podcast_id)
            profile = self.request.user.profile.first()
        except Exception as e:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        Comment.objects.create(podcast=podcast, profile=profile, **serializer.data).save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CommentComplaintCreateView(generics.CreateAPIView):
    queryset = CommentComplaint.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = PodcastCommentComplaintSerializer

    def post(self, request, comment_id, *args, **kwargs):
        try:
            comment = Comment.objects.filter(is_active=True).get(pk=comment_id)
            profile = self.request.user.profile.first()
        except Exception as e:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        CommentComplaint.objects.create(comment=comment, profile=profile, **serializer.data).save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CommentLikedView(generics.RetrieveAPIView):
    queryset = Comment.objects.filter(is_active=True)
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, pk, *args, **kwargs):
        user = self.request.user
        return Response(
            perform_object_liked_disliked(
                object_id=pk, ObjectModel=Comment, queryset=self.queryset, user=user, liked=True
            )
        )


class CommentDislikedView(generics.RetrieveAPIView):
    queryset = Comment.objects.filter(is_active=True)
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, pk, *args, **kwargs):
        user = self.request.user
        return Response(
            perform_object_liked_disliked(
                object_id=pk, ObjectModel=Comment, queryset=self.queryset, user=user, liked=False
            )
        )
