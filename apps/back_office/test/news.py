from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from rest_framework.test import APITestCase
from apps.news.choices import NewsStatusChoices, NewsStyleChoices, NewsTypeChoices
from apps.news.models import News, NewsCategory, NewsTag
from apps.users.choices import Role
from apps.users.models import User, Profile


class BackOfficeNewsTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            phone_number="+998935036638",
            password="new_pass",
        )
        self.profile = Profile.objects.create(user=self.user, info="User info", role=Role.author)
        self.uploaded_file_png = SimpleUploadedFile("cover.jpg", b"file_content", content_type="image/jpeg")

        self.category = NewsCategory.objects.create(name="Cat 1")
        self.news = News.objects.create(
            title="Title",
            style=NewsStyleChoices.STYLE_1,
            status=NewsStatusChoices.DRAFT,
            author=self.user,
            is_verified=True,
            cover=self.uploaded_file_png,
            type=NewsTypeChoices.NEWS,
            category=self.category,
        )
        self.tag = NewsTag.objects.create(name="Tag 1")

    def test_news_list(self):
        data = {
            "phone_number": "+998935036638",
            "password": "new_pass",
        }
        url = reverse("login")
        login = self.client.post(url, data, format="json")

        access_token = login.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")

        url = reverse("back_news_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 1)

    def test_news_create(self):
        data = {
            "phone_number": "+998935036638",
            "password": "new_pass",
        }
        url = reverse("login")
        login = self.client.post(url, data, format="json")

        access_token = login.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")

        url = reverse("back_news_create")
        data = {
            "title": "News title",
            "status": NewsStatusChoices.DRAFT,
            "author": self.user,
            "style": NewsStyleChoices.STYLE_1,
            "is_verified": True,
            "cover": self.uploaded_file_png,
            "type": NewsTypeChoices.NEWS,
            "category": self.category,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(News.objects.count(), 2)

    def test_news_detail(self):
        data = {
            "phone_number": "+998935036638",
            "password": "new_pass",
        }
        url = reverse("login")
        login = self.client.post(url, data, format="json")

        access_token = login.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")

        url = reverse(
            "back_news_detail",
            kwargs={"pk": self.news.id},
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(News.objects.count(), 1)

    def test_news_put(self):
        data = {
            "phone_number": "+998935036638",
            "password": "new_pass",
        }
        url = reverse("login")
        login = self.client.post(url, data, format="json")

        access_token = login.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")

        url = reverse(
            "back_news_update",
            kwargs={"pk": self.news.id},
        )
        data = {
            "title": "New Title",
            "author": self.user.id,
            "style": NewsStyleChoices.STYLE_1,
            "cover": "test.png",
            "type": NewsTypeChoices.NEWS,
            "category": self.category,
            "tags": [self.tag.id],
        }
        response = self.client.put(url, data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["title"], "New Title")

    def test_news_patch(self):
        data = {
            "phone_number": "+998935036638",
            "password": "new_pass",
        }
        url = reverse("login")
        login = self.client.post(url, data, format="json")

        access_token = login.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")

        url = reverse(
            "back_news_update",
            kwargs={"pk": self.news.id},
        )
        data = {"title": "New Title"}
        response = self.client.patch(url, data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["title"], "New Title")

    def test_news_delete(self):
        data = {
            "phone_number": "+998935036638",
            "password": "new_pass",
        }
        url = reverse("login")
        login = self.client.post(url, data, format="json")

        access_token = login.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")

        url = reverse(
            "back_news_delete",
            kwargs={"pk": self.news.id},
        )
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(News.objects.count(), 0)
