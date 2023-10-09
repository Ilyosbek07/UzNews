from django_filters import rest_framework as filters
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView

from apps.interview.models import Interview, InterviewTag
from apps.interview.serializers import (InterviewSerializer,
                                        InterviewTagSerializer)


class InterviewTagListAPIView(generics.ListAPIView):
    queryset = InterviewTag.objects.all()
    serializer_class = InterviewTagSerializer


class InterviewListAPIView(generics.ListAPIView):
    queryset = Interview.objects.order_by("-created_at")
    serializer_class = InterviewSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ("category", "in_stock")


class InterviewRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer


class RelatedInterviewListAPIView(APIView):
    def get(self):
        post = get_object_or_404(
            Interview,
            status=Post.Status.PUBLISHED,
            slug=post,
            publish__year=year,
            publish__month=month,
            publish__day=day,
        )
        # List of active comments for this post
        comments = post.comments.filter(active=True)
        form = CommentForm()
        # List of similar posts
        post_tags_ids = post.tags.values_list("id", flat=True)
        similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
        similar_posts = similar_posts.annotate(same_tags=Count("tags")).order_by("-same_tags", "-publish")[:4]
        return render(
            request,
            "blog/post/detail.html",
            {"post": post, "comments": comments, "form": form, "similar_posts": similar_posts},
        )
