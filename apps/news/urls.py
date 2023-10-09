from django.urls import path

from apps.news.views.article import MainArticleViewSet
from apps.news.views.news import (AllNewsViewSet, MainNewsViewSet,
                                  NewsCategoryListViewSet,
                                  PopularAndDiscussedNewsViewSet,
                                  TimeLineNewsListViewSet)

urlpatterns = [
    path("main_news/", MainNewsViewSet.as_view(), name="main-news"),
    path("main_articles/", MainArticleViewSet.as_view(), name="main-articles"),
    path(
        "popular_and_discussed_news/",
        PopularAndDiscussedNewsViewSet.as_view(),
        name="popular_and_discussed_news",
    ),
    path("all_news/", AllNewsViewSet.as_view(), name="all_news"),
    path(
        "news_category_list/",
        NewsCategoryListViewSet.as_view(),
        name="news_category_list",
    ),
    path(
        "timeline_news_list/",
        TimeLineNewsListViewSet.as_view(),
        name="timeline_news_list",
    ),
]
