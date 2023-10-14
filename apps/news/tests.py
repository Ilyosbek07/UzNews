from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from rest_framework.test import APITestCase

from apps.interview.choices import InterviewStyleStatusChoices, StatusChoices
from apps.interview.models import Interview
from apps.news.choices import NewsStatusChoices, NewsPositionChoices, NewsTypeChoices, NewsStyleChoices
from apps.news.models import News, NewsCategory
from apps.users.models import User


class NewsTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            password="test_password",
            phone_number="+998901234567",
            first_name="test_user",
        )
        self.category = NewsCategory.objects.create(name="News Category")
        self.uploaded_file = SimpleUploadedFile(
            "test_file.txt", b"Test content for the file", content_type="text/plain"
        )
        self.news = News.objects.create(
            title="News Title",
            author=self.user,
            is_verified=True,
            cover=self.uploaded_file,
            category=self.category,
            status=NewsStatusChoices.DRAFT,
            position=NewsPositionChoices.ORDINARY,
            type=NewsTypeChoices.NEWS,
            style=NewsStyleChoices.STYLE_1,
        )

    def test_news_list(self):
        url = reverse("main-news")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(News.objects.count(), 1)

    # def test_interview_detail(self):
    #     url = reverse(
    #         "interview-detail",
    #         kwargs={"pk": self.interview.id},
    #     )
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(Interview.objects.count(), 1)


#
