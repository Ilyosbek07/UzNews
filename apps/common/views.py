from rest_framework import generics
from apps.common.models import Advertising, SocialMedia
from apps.common.serializers import AdvertisingSerializer, SocialMediaSerializer


class AdvertisingListAPIView(generics.ListAPIView):
    queryset = Advertising.objects.all()
    serializer_class = AdvertisingSerializer


class SocialMediaListAPIView(generics.ListAPIView):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer
