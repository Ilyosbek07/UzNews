from django.urls import path

from .views import NewPodcastsView, PodcastTagCreateView, PodcastTagListView

urlpatterns = [
    path("tags/", PodcastTagListView.as_view(), name="tags_list"),
    path("tags/create/", PodcastTagCreateView.as_view(), name="tag_create"),
    path("podcasts/new/", NewPodcastsView.as_view(), name="new_podcasts_list"),
]
