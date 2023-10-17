from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.opinion.choices import OpinionStatusChoices
from apps.opinion.models import Category, Comment, Opinion
from apps.users.models import Profile, User


class OpinionListAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(phone_number="+998987654321", password="test_pass_12345")
        self.profile = Profile.objects.create(user=self.user)
        self.category = Category.objects.create(name="test category", icon="test_icon.svg")
        self.opinion = Opinion.objects.create(
            title="test title",
            subtitle="test subtitle",
            status=OpinionStatusChoices.PUBLISHED,
            category=self.category,
        )

    def test_list_opinions(self):
        response = self.client.get(reverse("opinion:new_opinions_list"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)
        self.assertEqual(response.data["results"][0]["title"], self.opinion.title)

    def test_detail_opinion(self):
        response = self.client.get(reverse("opinion:opinion_detail", kwargs={"slug": self.opinion.slug}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.opinion.title)

    def test_create_comment(self):
        logged_in = self.client.login(phone_number="+998987654321", password="test_pass_12345")
        self.assertTrue(logged_in)

        data = {"text": "test comment", "profile": self.profile}
        response = self.client.post(reverse("opinion:comment_create", kwargs={"opinion_id": self.opinion.id}), data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_comment(self):
        logged_in = self.client.login(phone_number="+998987654321", password="test_pass_12345")
        self.assertTrue(logged_in)

        Comment.objects.create(opinion=self.opinion, profile=self.profile, text="test comment")

        response = self.client.get(reverse("opinion:opinion_comments", kwargs={"opinion_id": self.opinion.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)
        self.assertEqual(response.data["results"][0]["text"], "test comment")

    def test_opinion_liked(self):
        logged_in = self.client.login(phone_number="+998987654321", password="test_pass_12345")
        self.assertTrue(logged_in)

        response = self.client.get(reverse("opinion:opinion_liked", kwargs={"pk": self.opinion.id}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.opinion.get_like_dislike_count(), {"like": 1, "dislike": 0})
