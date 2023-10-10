from django.db.models import Count
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from apps.news.choices import NewsTypeChoices
from apps.news.filters import NewsFilter
from apps.news.models import News, NewsCategory
from apps.news.serializers import (NewsCategorySerializer, NewsSerializer,
                                   TimeLineNewsSerializer)


class MainNewsViewSet(ListAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.all()

    def list(self, request, *args, **kwargs):
        prime_news = News.objects.filter(position="prime", status="published").order_by("-created_at")[:3]
        main_news = News.objects.filter(position="main", status="published").order_by("-created_at")[:4]
        main_news_serializer = NewsSerializer(main_news, many=True)
        prime_news_serializer = NewsSerializer(prime_news, many=True)

        response_data = {
            "prime_news": main_news_serializer.data,
            "main_news": prime_news_serializer.data,
        }

        return Response(response_data, status=status.HTTP_200_OK)


class PopularAndDiscussedNewsViewSet(ListAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.all()

    def list(self, request, *args, **kwargs):
        popular_news = (
            News.objects.filter(status="published")
            .annotate(num_views=Count("news_view_to_news"))
            .order_by("-num_views")[:7]
        )
        discussed_news = (
            News.objects.filter(status="published")
            .annotate(num_comments=Count("news_comment_to_news"))
            .order_by("-num_comments")[:7]
        )
        popular_news_serializer = NewsSerializer(popular_news, many=True)
        discussed_news_serializer = NewsSerializer(discussed_news, many=True)

        response_data = {
            "popular_news": popular_news_serializer.data,
            "discussed_news": discussed_news_serializer.data,
        }

        return Response(response_data, status=status.HTTP_200_OK)


class AllNewsViewSet(ListAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.filter(status="published", type=NewsTypeChoices.NEWS)
    filterset_class = NewsFilter


class TimeLineNewsListViewSet(ListAPIView):
    serializer_class = TimeLineNewsSerializer
    queryset = News.objects.all().order_by("-created_at")


class NewsCategoryListViewSet(ListAPIView):
    serializer_class = NewsCategorySerializer
    queryset = NewsCategory.objects.all()
