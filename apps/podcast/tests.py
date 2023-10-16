from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.podcast.choices import PodcastStatusChoices
from apps.podcast.models import Category, Comment, Podcast
from apps.users.models import Profile, User


class PodcastListAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(phone_number="+998987654321", password="test_pass_12345")
        self.profile = Profile.objects.create(user=self.user)
        self.category = Category.objects.create(name="test category", icon="test_icon.svg")
        self.podcast = Podcast.objects.create(
            title="test title",
            subtitle="test subtitle",
            status=PodcastStatusChoices.PUBLISHED,
            file="test_audio.mp3",
            category=self.category,
        )

    def test_list_podcasts(self):
        response = self.client.get(reverse("podcast:new_podcasts_list"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)
        self.assertEqual(response.data["results"][0]["title"], self.podcast.title)

    def test_detail_podcast(self):
        response = self.client.get(reverse("podcast:podcast_detail", kwargs={"slug": self.podcast.slug}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.podcast.title)

    def test_create_comment(self):
        logged_in = self.client.login(phone_number="+998987654321", password="test_pass_12345")
        self.assertTrue(logged_in)

        data = {"text": "test comment", "profile": self.profile}
        response = self.client.post(reverse("podcast:comment_create", kwargs={"podcast_id": self.podcast.id}), data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_comment(self):
        logged_in = self.client.login(phone_number="+998987654321", password="test_pass_12345")
        self.assertTrue(logged_in)

        Comment.objects.create(podcast=self.podcast, profile=self.profile, text="test comment")

        response = self.client.get(reverse("podcast:podcast_comments", kwargs={"podcast_id": self.podcast.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)
        self.assertEqual(response.data["results"][0]["text"], "test comment")

    def test_podcast_liked(self):
        logged_in = self.client.login(phone_number="+998987654321", password="test_pass_12345")
        self.assertTrue(logged_in)

        response = self.client.get(reverse("podcast:podcast_liked", kwargs={"pk": self.podcast.id}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.podcast.get_like_dislike_count(), {"like": 1, "dislike": 0})
