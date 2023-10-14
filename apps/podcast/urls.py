from django.urls import path

from .views import NewPodcastsView, TagCreateView, TagListView

urlpatterns = [
    path("tags/", TagListView.as_view(), name="tags_list"),
    path("tags/create/", TagCreateView.as_view(), name="tag_create"),
    path("podcasts/new/", NewPodcastsView.as_view(), name="new_podcasts_list"),
]
