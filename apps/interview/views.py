from django.shortcuts import get_object_or_404
from rest_framework import filters, generics, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.interview.models import Interview, InterviewTag, InterviewView, InterviewLike
from apps.interview.serializers import (InterviewSerializer,
                                        InterviewTagSerializer, InterviewDetailSerializer)
from apps.interview.utils import perform_disliked, perform_liked


class InterviewTagListAPIView(generics.ListAPIView):
    queryset = InterviewTag.objects.all()
    serializer_class = InterviewTagSerializer


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
        interview = get_object_or_404(queryset, id=self.kwargs["pk"])
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
        try:
            obj = self.get_queryset().get(id=pk)
            selected_product_tags = obj.tag.all()
            related_products = (
                self.get_queryset()
                .filter(tag__in=selected_product_tags)
                .exclude(id=pk)
                .distinct()
            )
            related_products_list = list(related_products)
            random_related_products = related_products_list[:4]
            serializer = self.serializer_class(
                instance=random_related_products, many=True
            )
            return Response(serializer.data)
        except Interview.DoesNotExist:
            return Response({"message": "Interview not found."}, status=404)


class InterviewLikedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        profile = self.request.user.profile
        try:
            content = Interview.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        perform_liked(profile, content, InterviewLike)
        return Response(status=status.HTTP_200_OK)


class InterviewDislikedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        profile = self.request.user.profile
        try:
            content = Interview.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        perform_disliked(profile, content, InterviewLike)
        return Response(status=status.HTTP_200_OK)
