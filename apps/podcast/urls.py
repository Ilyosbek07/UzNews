from django.urls import path

from .views import (CommentComplaintCreateView, CommentCreateView,
                    CommentDislikedView, CommentLikedView,
                    MostCommentedPodcastsView, MostViewedPodcastsView,
                    NewPodcastsView, PodcastCommentsView, PodcastDetailView,
                    PodcastDislikedView, PodcastLikedView,
                    PodcastSuggestionsView, PodcastTagListView)

app_name = "podcast"

urlpatterns = [
    path("tags/", PodcastTagListView.as_view(), name="tags_list"),
    path("podcasts/new/", NewPodcastsView.as_view(), name="new_podcasts_list"),
    path("podcasts/most_viewed/", MostViewedPodcastsView.as_view(), name="most_viewed_podcasts"),
    path("podcasts/most_commented/", MostCommentedPodcastsView.as_view(), name="most_commented_podcasts"),
    path("podcasts/<slug:slug>/", PodcastDetailView.as_view(), name="podcast_detail"),
    path("podcasts/suggestions/<int:podcast_id>/", PodcastSuggestionsView.as_view(), name="podcast_suggestions"),
    path("podcasts/liked/<int:pk>/", PodcastLikedView.as_view(), name="podcast_liked"),
    path("podcasts/disliked/<int:pk>/", PodcastDislikedView.as_view(), name="podcast_disliked"),
    path("comments/create/<int:podcast_id>/", CommentCreateView.as_view(), name="comment_create"),
    path("comments/liked/<int:pk>/", CommentLikedView.as_view(), name="comment_liked"),
    path("comments/disliked/<int:pk>/", CommentDislikedView.as_view(), name="comment_disliked"),
    path(
        "comment_complaints/create/<int:comment_id>/",
        CommentComplaintCreateView.as_view(),
        name="comment_complaint_create",
    ),
    path("comments/podcast/<int:podcast_id>/", PodcastCommentsView.as_view(), name="podcast_comments"),
]
