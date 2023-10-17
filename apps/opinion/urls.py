from django.urls import path

from .views import (CommentComplaintCreateView, CommentCreateView,
                    CommentDislikedView, CommentLikedView,
                    MostCommentedOpinionsView, MostViewedOpinionsView,
                    NewOpinionsView, OpinionCommentsView, OpinionDetailView,
                    OpinionDislikedView, OpinionLikedView,
                    OpinionSuggestionsView, OpinionTagListView)

app_name = "opinion"

urlpatterns = [
    path("tags/", OpinionTagListView.as_view(), name="tags_list"),
    path("opinions/new/", NewOpinionsView.as_view(), name="new_opinions_list"),
    path("opinions/most_viewed/", MostViewedOpinionsView.as_view(), name="most_viewed_opinions"),
    path("opinions/most_commented/", MostCommentedOpinionsView.as_view(), name="most_commented_opinions"),
    path("opinions/<slug:slug>/", OpinionDetailView.as_view(), name="opinion_detail"),
    path("opinions/suggestions/<int:podcast_id>/", OpinionSuggestionsView.as_view(), name="opinion_suggestions"),
    path("opinions/liked/<int:pk>/", OpinionLikedView.as_view(), name="opinion_liked"),
    path("opinions/disliked/<int:pk>/", OpinionDislikedView.as_view(), name="opinion_disliked"),
    path("comments/create/<int:opinion_id>/", CommentCreateView.as_view(), name="comment_create"),
    path("comments/liked/<int:pk>/", CommentLikedView.as_view(), name="comment_liked"),
    path("comments/disliked/<int:pk>/", CommentDislikedView.as_view(), name="comment_disliked"),
    path(
        "comment_complaints/create/<int:comment_id>/",
        CommentComplaintCreateView.as_view(),
        name="comment_complaint_create",
    ),
    path("comments/opinion/<int:opinion_id>/", OpinionCommentsView.as_view(), name="opinion_comments"),
]
