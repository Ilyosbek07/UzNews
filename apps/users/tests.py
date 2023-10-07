from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.users.choices import Role
from apps.users.models import Profile, User


class UserAPITestCase(APITestCase):
    def setUp(self):
        self.phone_number = "+998987654321"
        self.password = "my_pass"
        self.user = User.objects.create_user(phone_number="+998644321232", password="my_pass123")
        self.profile = Profile.objects.create(
            user=self.user,
            surname="Karshiboyev",
            info="Info",
            role=Role.simple_user,
        )

    def test_user_register(self):
        data = {
            "first_name": "Ilyos",
            "phone_number": "+998987654321",
            "password": "my_pass$001",
        }
        url = reverse("user_register")
        response = self.client.post(url, data=data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)

        self.assertEqual(response.data["phone_number"], data["phone_number"])

    def test_user_login(self):
        data = {
            "phone_number": "+998644321232",
            "password": "my_pass123",
        }
        url = reverse("login")
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("refresh", response.data)
        self.assertIn("access", response.data)

    def test_get_profile(self):
        data = {
            "phone_number": "+998644321232",
            "password": "my_pass123",
        }
        url = reverse("login")
        login = self.client.post(url, data, format="json")

        access_token = login.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")
        get_profile_url = reverse("profile")
        response = self.client.get(get_profile_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
