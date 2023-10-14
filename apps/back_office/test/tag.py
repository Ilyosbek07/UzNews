from django.urls import reverse
from rest_framework.test import APITestCase

from apps.common.models import Tag
from apps.interview.choices import StatusChoices, InterviewStyleStatusChoices
from apps.interview.models import Interview
from apps.users.choices import Role
from apps.users.models import User, Profile


class BackOfficeTagTestCase(APITestCase):
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

        self.tag = Tag.objects.create(name="Tag 1")

    def test_interview_create(self):
        data = {
            "phone_number": "+998935036638",
            "password": "new_pass",
        }
        url = reverse("login")
        login = self.client.post(url, data, format="json")

        access_token = login.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")

        url = reverse("back_tag_create")
        data = {
            "name": "Tag 2",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Tag.objects.count(), 2)
    #
    # def test_interview_put(self):
    #     data = {
    #         "phone_number": "+998935036638",
    #         "password": "new_pass",
    #     }
    #     url = reverse("login")
    #     login = self.client.post(url, data, format="json")
    #
    #     access_token = login.data["access"]
    #     self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")
    #
    #     url = reverse(
    #         "back_tag_update",
    #         kwargs={"pk": self.tag.id},
    #     )
    #     data = {
    #         "name": "New Tag",
    #     }
    #     response = self.client.put(url, data=data)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.data["title"], "New Tag")

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
            "back_tag_delete",
            kwargs={"pk": self.tag.id},
        )
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Interview.objects.count(), 0)
#