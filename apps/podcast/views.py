from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .utils import perform_liked, perform_disliked
from .models import Podcast, UserPodcastPreference

class PodcastLikedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, format=None):
        profile = self.request.user.profile
        try:
            content = Podcast.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        perform_liked(profile, content, UserPodcastPreference)
        return Response(status=status.HTTP_200_OK)


class PodcastDislikedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, format=None):
        profile = self.request.user.profile
        try:
            content = Podcast.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        perform_disliked(profile, content, UserPodcastPreference)
        return Response(status=status.HTTP_200_OK)
    