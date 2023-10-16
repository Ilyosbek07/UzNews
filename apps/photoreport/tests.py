from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.photoreport.models import Comment, PhotoReport
from apps.users.models import User


class PhotoReportListAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(phone_number="+998644321232", password="my_pass123")

        self.photoreport = PhotoReport.objects.create(
            title="test1",
            slug="test1",
            desc="testdesc1",
        )

    def test_list_photo_reports(self):
        response = self.client.get(reverse("photo_report_list"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)
        self.assertEqual(response.data["results"][0]["title"], self.photoreport.title)

    def test_detail_photo_reports(self):
        response = self.client.get(reverse("photo_report_detail", kwargs={"slug": self.photoreport.slug}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.photoreport.title)

    def test_create_comment(self):
        logged_in = self.client.login(phone_number="+998644321232", password="my_pass123")

        self.assertTrue(logged_in)

        data = {"text": "Comment1", "user": self.user.id}
        response = self.client.post(reverse("comment_create", kwargs={"slug": self.photoreport.slug}), data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_comment(self):
        logged_in = self.client.login(phone_number="+998644321232", password="my_pass123")

        self.assertTrue(logged_in)
        for i in range(2):
            Comment.objects.create(photo_report=self.photoreport, user=self.user, text=f"comment{i}")

        response = self.client.get(reverse("photo_report_comments", kwargs={"slug": self.photoreport.slug}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 2)
        self.assertEqual(response.data["results"][0]["text"], "comment0")
        self.assertEqual(response.data["results"][1]["text"], "comment1")

    def test_prime_photoreport(self):
        logged_in = self.client.login(phone_number="+998644321232", password="my_pass123")

        self.assertTrue(logged_in)

        PhotoReport.objects.create(title="test1", slug="test1", desc="testdesc1", author=self.user, is_prime=True)
        response = self.client.get(reverse("prime_photo_report"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["results"][0]["title"], "test1")
