from django.urls import reverse
from rest_framework.test import APITestCase

from apps.common.models import Tag
from apps.interview.choices import StatusChoices, InterviewStyleStatusChoices
from apps.interview.models import Interview
from apps.users.choices import Role
from apps.users.models import User, Profile


class BackOfficeInterviewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            phone_number="+998935036638",
            password="new_pass",
        )
        self.profile = Profile.objects.create(user=self.user, info="User info", role=Role.author)

        self.interview = Interview.objects.create(
            title="Title",
            style_type=InterviewStyleStatusChoices.STYLE_1,
            status=StatusChoices.DRAFT,
            subtitle="Subtitle Test",
            video_url="https://www.figma.com/file/",
        )
        self.tag = Tag.objects.create(name="Tag 1")

    def test_interview_list(self):
        data = {
            "phone_number": "+998935036638",
            "password": "new_pass",
        }
        url = reverse("login")
        login = self.client.post(url, data, format="json")

        access_token = login.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")

        url = reverse("back_interview_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 1)

    def test_interview_create(self):
        data = {
            "phone_number": "+998935036638",
            "password": "new_pass",
        }
        url = reverse("login")
        login = self.client.post(url, data, format="json")

        access_token = login.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")

        url = reverse("back_interview_create")
        data = {
            "title": "New Interview",
            "subtitle": "New Subtitle",
            "status": "published",
            "video_url": "http://127.0.0.1:8000/swagger/",
            "tag": [self.tag.id],
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Interview.objects.count(), 2)

    def test_interview_detail(self):
        data = {
            "phone_number": "+998935036638",
            "password": "new_pass",
        }
        url = reverse("login")
        login = self.client.post(url, data, format="json")

        access_token = login.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")

        url = reverse(
            "back_interview_detail",
            kwargs={"pk": self.interview.id},
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Interview.objects.count(), 1)

    def test_interview_put(self):
        data = {
            "phone_number": "+998935036638",
            "password": "new_pass",
        }
        url = reverse("login")
        login = self.client.post(url, data, format="json")

        access_token = login.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")

        url = reverse(
            "back_interview_update",
            kwargs={"pk": self.interview.id},
        )
        data = {
            "title": "New Title",
            "subtitle": "New Sub Title",
            "status": "published",
            "video_url": "http://127.0.0.1:8080/swagger/",
            "tag": [self.tag.id],
        }
        response = self.client.put(url, data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["title"], "New Title")
        self.assertEqual(response.data["subtitle"], "New Sub Title")

    def test_interview_patch(self):
        data = {
            "phone_number": "+998935036638",
            "password": "new_pass",
        }
        url = reverse("login")
        login = self.client.post(url, data, format="json")

        access_token = login.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")

        url = reverse(
            "back_interview_update",
            kwargs={"pk": self.interview.id},
        )
        data = {"title": "New Title"}
        response = self.client.patch(url, data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["title"], "New Title")

    def test_interview_delete(self):
        data = {
            "phone_number": "+998935036638",
            "password": "new_pass",
        }
        url = reverse("login")
        login = self.client.post(url, data, format="json")

        access_token = login.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")

        url = reverse(
            "back_interview_delete",
            kwargs={"pk": self.interview.id},
        )
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Interview.objects.count(), 0)
