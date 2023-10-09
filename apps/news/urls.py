from django.urls import path

from apps.news.views import MainNewsViewSet, PopularAndDiscussedNewsViewSet

urlpatterns = [
    path("main_news/", MainNewsViewSet.as_view(), name="main-news"),
    path("popular_and_discussed_news/", PopularAndDiscussedNewsViewSet.as_view(), name="popular_and_discussed_news"),
]
