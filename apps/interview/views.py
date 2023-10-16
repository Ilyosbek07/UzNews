from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, status
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.common.models import ContentLike
from apps.interview.models import Comment, CommentLike
from apps.interview.serializers import (Interview,
                                        InterviewCommentCreateSerializer,
                                        InterviewCommentsListSerializer,
                                        InterviewCreateSerializer,
                                        InterviewDetailSerializer,
                                        InterviewLikeDislikeSerializer,
                                        InterviewSerializer)


class InterviewListAPIView(generics.ListAPIView):
    queryset = Interview.objects.order_by("-created_at")
    serializer_class = InterviewSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ("title",)
    filterset_fields = ("tag", "status")


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


class InterviewCommentsListAPIView(generics.ListAPIView):
    serializer_class = InterviewCommentsListSerializer

    def get_queryset(self):
        slug = self.kwargs.get("slug")
        return Comment.objects.filter(interview__slug=slug, parent=None)


class InterviewCommentCreateAPIView(generics.CreateAPIView):
    serializer_class = InterviewCommentCreateSerializer
    parser_classes = (MultiPartParser,)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        interview = Interview.objects.get(slug=self.kwargs.get("slug"))
        text = serializer.validated_data.get("text")
        image = serializer.validated_data.get("image")
        parent = serializer.validated_data.get("parent")

        comment = Comment.objects.create(interview=interview, user=request.user, text=text, image=image, parent=parent)

        response_serializer = self.serializer_class(comment)

        return Response(response_serializer.data, status=status.HTTP_201_CREATED)


class InterviewLikeDislikeAPIView(generics.CreateAPIView):
    serializer_class = InterviewLikeDislikeSerializer

    def post(self, request, *args, **kwargs):
        slug = self.kwargs.get("slug")
        interview = get_object_or_404(Interview, slug=slug)
        type = request.data["type"]
        user = request.user
        if type == "like":
            like = ContentLike.objects.filter(
                content_type=ContentType.objects.get_for_model(interview),
                object_id=interview.id,
                user=user,
                status="d",
            )
            if like.exists():
                like.update(status="l")
                return Response({"message": "Interview liked updated."}, status=status.HTTP_201_CREATED)
            try:
                ContentLike.objects.create_for_object(interview, request.user, status="l")
                return Response(
                    {"message": "Interview liked create successfully."},
                    status=status.HTTP_201_CREATED,
                )
            except:
                return Response({"message": "Interview liked already have. "})

        elif type == "dislike":
            dislike = ContentLike.objects.filter(
                content_type=ContentType.objects.get_for_model(interview),
                object_id=interview.id,
                user=user,
                status="l",
            )
            if dislike.exists():
                dislike.update(status="d")
                return Response(
                    {"message": "Interview disliked updated."},
                    status=status.HTTP_201_CREATED,
                )
            try:
                ContentLike.objects.create_for_object(interview, request.user, status="d")
                return Response(
                    {"message": "Interview disliked create successfully."},
                    status=status.HTTP_200_OK,
                )
            except:
                return Response({"message": "Interview disliked already have. "})


class InterviewCommentLikeDislikeAPIView(APIView):
    def post(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, id=self.kwargs["id"])
        if request.user.is_authenticated:
            data = CommentLike.objects.filter(user=request.user, comment=comment)
            if data.exists():
                CommentLike.objects.filter(user=request.user, comment=comment).delete()
                comment.liked -= 1
                comment.save()
                return Response({"message": "successfully deleted. "})
            else:
                CommentLike.objects.create(user=request.user, comment=comment)
                comment.liked += 1
                return Response({"message": "successfully created. "})
        return Response({"message": "error"})
