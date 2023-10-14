from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.common.models import Tag
from apps.interview.choices import StatusChoices, InterviewStyleStatusChoices
from apps.interview.models import Interview
from apps.users.choices import Role
from apps.users.models import User, Profile


class BackOfficeProfileTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            phone_number='+998935036638',
            password='new_pass',
        )
        self.profile = Profile.objects.create(
            user=self.user,
            info='User info',
            role=Role.author
        )

    def test_profile_list(self):
        url = reverse("back_profile_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 1)

    def test_get_profile(self):
        data = {
            "phone_number": "+998935036638",
            "password": "new_pass",
        }
        url = reverse("login")
        login = self.client.post(url, data, format="json")

        access_token = login.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")
        get_profile_url = reverse("back_profile_detail")
        response = self.client.get(get_profile_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_put(self):
        url = reverse(
            "back_profile_update",
            kwargs={"pk": self.profile.id},
        )
        data = {
            "user": self.user,
            "info": "New Info",
        }
        response = self.client.put(url, data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["info"], "New Info")

    def test_profile_patch(self):
        url = reverse(
            "back_profile_update",
            kwargs={"pk": self.profile.id},
        )
        data = {"info": "New Info 2"}
        response = self.client.patch(url, data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["info"], "New Info 2")

    def test_profile_delete(self):
        url = reverse(
            "back_profile_delete",
            kwargs={"pk": self.profile.id},
        )
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Profile.objects.count(), 0)
