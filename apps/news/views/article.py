from django.db.models import Count
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from apps.news.choices import NewsStatusChoices, NewsTypeChoices
from apps.news.filters import ArticleFilter
from apps.news.models import News
from apps.news.serializers import NewsSerializer


class MainArticleViewSet(ListAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.all()

    def list(self, request, *args, **kwargs):
        popular_articles = (
            News.objects.filter(status=NewsStatusChoices.PUBLISHED, type=NewsTypeChoices.ARTICLE)
            .annotate(num_views=Count("news_view_to_news"))
            .order_by("-num_views")[:5]
        )
        popular_articles_serializer = NewsSerializer(popular_articles, many=True)
        response_data = {
            "popular_articles": popular_articles_serializer.data,
        }

        return Response(response_data, status=status.HTTP_200_OK)


class AllArticlesViewSet(ListAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.filter(status=NewsStatusChoices.PUBLISHED, type=NewsTypeChoices.ARTICLE)
    filterset_class = ArticleFilter


class SuggestedArticlesViewSet(ListAPIView):
    serializer_class = NewsSerializer
    lookup_field = "pk"

    def get_queryset(self):
        article_id = self.kwargs.get("pk")
        news_article = get_object_or_404(News, id=article_id, type=NewsTypeChoices.ARTICLE)
        if news_article:
            tags = news_article.tags.all()
            suggested_articles = (
                News.objects.filter(tags__in=tags, type=NewsTypeChoices.ARTICLE).exclude(id=article_id).distinct()[:3]
            )
            return suggested_articles
