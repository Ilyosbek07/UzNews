import requests
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.common.models import Advertising, SocialMedia, Tag
from apps.common.serializers import (
    AdvertisingSerializer,
    SocialMediaSerializer,
    TagSerializer,
)


class AdvertisingListAPIView(generics.ListAPIView):
    queryset = Advertising.objects.all()
    serializer_class = AdvertisingSerializer


class SocialMediaListAPIView(generics.ListAPIView):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer


class TagListAPIView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


@api_view(['GET'])
def get_exchange_rate(request):
    response = requests.get("https://nbu.uz/uz/exchange-rates/json/")
    if response.status_code == 200:
        return Response(status=status.HTTP_200_OK, data=response.json())
    return Response(status=status.HTTP_404_NOT_FOUND)
