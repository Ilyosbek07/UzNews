from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.back_office.permissions import IsAuthor
from apps.common.models import Tag
from apps.common.serializers import TagSerializer


class TagCreateAPIView(generics.CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (IsAuthenticated, IsAuthor)


class TagUpdateAPIView(generics.UpdateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (IsAuthenticated, IsAuthor)


class TagDestroyAPIView(generics.DestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (IsAuthenticated, IsAuthor)
