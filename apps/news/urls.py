from django.urls import path
from apps.news.views import MainNewsViewSet

urlpatterns = [
    path("main_news/", MainNewsViewSet.as_view(), name="main-news"),
]
