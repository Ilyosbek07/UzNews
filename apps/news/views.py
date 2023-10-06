from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from apps.news.models import News
from apps.news.serializers import NewsSerializer


class MainNewsViewSet(ListAPIView):
    serializer = NewsSerializer
    model = News.objects.filter()

    def get(self, request, *args, **kwargs):
        main_news = News.objects.filter(position="main")[:4]
        prime_news = News.objects.filter(position="prime").order_by("-created_at")[:3]

        main_news_serializer = NewsSerializer(main_news, many=True)
        prime_news_serializer = NewsSerializer(prime_news, many=True)

        response_data = {
            "prime_news": main_news_serializer.data,
            "main_news": prime_news_serializer.data,
        }

        return Response(response_data, status=status.HTTP_200_OK)
