from rest_framework import generics

from apps.interview.models import Interview, InterviewTag
from apps.interview.serializers import InterviewSerializer, InterviewTagSerializer


class InterviewTagListAPIView(generics.ListAPIView):
    queryset = InterviewTag.objects.all()
    serializer_class = InterviewTagSerializer


class InterviewListAPIView(generics.ListAPIView):
    queryset = Interview.objects.order_by('-created_at')
    serializer_class = InterviewSerializer


class InterviewRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer
