from django.urls import reverse
from rest_framework import status, test

from apps.review.models import Category, Comment, Review
from apps.users.models import User


class CommonAPITestCase(test.APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(phone_number="+998991234567", password="testpassword1")
        self.client.login(phone_number="+998991234567", password="testpassword1")

        self.category = Category.objects.create(name="category1")

        self.data = Review.objects.create(title="test1", slug="test1", desc="test1", category=self.category)

        self.comment1 = Comment.objects.create(review=self.data, user=self.user, text="commenttest1")

    def test_review_list(self):
        response = self.client.get(reverse("review_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)
        self.assertEqual(response.data["results"][0]["title"], self.data.title)
        self.assertEqual(response.data["results"][0]["category"], self.category.id)

    def test_review_detail(self):
        response = self.client.get(reverse("review_detail", kwargs={"slug": self.data.slug}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.data.title)

    def test_review_related(self):
        self.data1 = Review.objects.create(title="test2", slug="test2", desc="test2", category=self.category)
        response = self.client.get(reverse("review_related", kwargs={"slug": self.data1.slug}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)
        self.assertEqual(response.data["results"][0]["title"], self.data.title)

    def test_review_comments(self):
        comment2 = Comment.objects.create(review=self.data, user=self.user, text="commenttest1")

        response = self.client.get(reverse("review_comments", kwargs={"slug": self.data.slug}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 2)
        self.assertEqual(response.data["results"][0]["text"], self.comment1.text)
        self.assertEqual(response.data["results"][1]["text"], comment2.text)

    # def test_comment_create(self):
    #     response = self.client.post(reverse("comment_create"))
