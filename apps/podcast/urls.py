from django.urls import path
from .views import PodcastLikedView, PodcastDislikedView

urlpatterns = [
    path("liked/<int:pk>/", PodcastLikedView.as_view(), name="podcast_liked"),
    path("disliked/<int:pk>/", PodcastDislikedView.as_view(), name="podcast_disliked")
]
