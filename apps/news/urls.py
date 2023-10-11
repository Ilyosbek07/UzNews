from django.urls import path

from apps.news.views.article import (AllArticlesViewSet, MainArticleViewSet,
                                     SuggestedArticlesViewSet)
from apps.news.views.news import (AllNewsViewSet,
                                  ArticleAndNewsRetrieveViewSet,
                                  MainNewsViewSet,
                                  NewsArticleCommentReportViewSet,
                                  NewsCategoryListViewSet,
                                  PopularAndDiscussedNewsViewSet,
                                  SuggestedNewsViewSet,
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
    path("all_articles/", AllArticlesViewSet.as_view(), name="all_articles"),
    path("news_article_detail/<int:pk>/", ArticleAndNewsRetrieveViewSet.as_view(), name="news_article_detail"),
    path("suggested_news/<int:pk>/", SuggestedNewsViewSet.as_view(), name="suggested_news"),
    # path("suggested_articles/<int:pk>/", SuggestedArticlesViewSet.as_view(), name="suggested_articles"),
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
    path("news_article_comment_report/", NewsArticleCommentReportViewSet.as_view(), name="news_article_comment_report"),
]
