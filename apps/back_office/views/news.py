from rest_framework import generics
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated

from apps.back_office.permissions import IsAuthor
from apps.back_office.serializers.news import BackOfficeNewsSerializer, BackOfficeNewsListSerializer
from apps.news.filters import NewsFilter
from apps.news.models import News
from apps.news.serializers import NewsSerializer


class NewsListAPIView(generics.ListAPIView):
    serializer_class = BackOfficeNewsListSerializer
    queryset = News.objects.all()
    filterset_class = NewsFilter
    permission_classes = (IsAuthenticated, IsAuthor)


class NewsRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = BackOfficeNewsSerializer
    queryset = News.objects.all()
    permission_classes = (IsAuthenticated, IsAuthor)


class NewsCreateAPIView(generics.CreateAPIView):
    serializer_class = BackOfficeNewsSerializer
    queryset = News.objects.all()
    parser_classes = (MultiPartParser,)
    permission_classes = (IsAuthenticated, IsAuthor)


class NewsUpdateAPIView(generics.UpdateAPIView):
    serializer_class = BackOfficeNewsSerializer
    queryset = News.objects.all()
    parser_classes = (MultiPartParser,)
    permission_classes = (IsAuthenticated, IsAuthor)


class NewsDestroyAPIView(generics.DestroyAPIView):
    serializer_class = BackOfficeNewsSerializer
    queryset = News.objects.all()
    permission_classes = (IsAuthenticated, IsAuthor)
