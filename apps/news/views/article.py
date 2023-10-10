from django.db.models import Count
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from apps.news.choices import NewsTypeChoices
from apps.news.models import News
from apps.news.serializers import NewsSerializer


class MainArticleViewSet(ListAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.all()

    def list(self, request, *args, **kwargs):
        popular_news = (
            News.objects.filter(status="published", type=NewsTypeChoices.ARTICLE)
            .annotate(num_views=Count("news_view_to_news"))
            .order_by("-num_views")[:5]
        )
        popular_news_serializer = NewsSerializer(popular_news, many=True)
        response_data = {
            "popular_articles": popular_news_serializer.data,
        }

        return Response(response_data, status=status.HTTP_200_OK)


class AllArticlesViewSet(ListAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.filter(status="published", type=NewsTypeChoices.ARTICLE)
