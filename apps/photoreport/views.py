from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

from apps.photoreport.models import Comment, CommentLike, PhotoReport
from apps.photoreport.serializers import (CommentCreateSerializer,
                                          CommentsListSerializer,
                                          PhotoReportDetailSerializer,
                                          PhotoReportListSerializer)


class PhotoReportListAPIView(generics.ListAPIView):
    queryset = PhotoReport.objects.all()
    serializer_class = PhotoReportListSerializer


class PhotoReportDetailAPIView(generics.RetrieveAPIView):
    queryset = PhotoReport.objects.all()
    serializer_class = PhotoReportDetailSerializer
    lookup_field = "slug"


class CommentsListAPIView(generics.ListAPIView):
    serializer_class = CommentsListSerializer

    def get_queryset(self):
        slug = self.kwargs.get("slug")
        return Comment.objects.filter(photo_report__slug=slug, parent=None)


class CommentCreateAPIView(generics.CreateAPIView):
    serializer_class = CommentCreateSerializer
    parser_classes = (MultiPartParser,)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        photo_report = PhotoReport.objects.get(slug=self.kwargs.get("slug"))
        text = serializer.validated_data.get("text")
        image = serializer.validated_data.get("image")
        parent = serializer.validated_data.get("parent")

        comment = Comment.objects.create(
            photo_report=photo_report, user=request.user, text=text, image=image, parent=parent
        )

        response_serializer = self.serializer_class(comment)

        return Response(response_serializer.data, status=status.HTTP_201_CREATED)


class CreateLikeCommentAPIView(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, id=self.kwargs["id"])
        if request.user.is_authenticated:
            CommentLike.objects.update_or_create(user=request.user, comment=comment)
            return Response({"message": "successfully created. "})
        return Response({"message": "error"})


class CreateDislikeCommentAPIView(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, id=self.kwargs["id"])
        if request.user.is_authenticated:
            CommentLike.objects.filter(user=request.user, comment=comment).delete()
            return Response({"message": "successfully deleted. "})
        return Response({"message": "error"})
