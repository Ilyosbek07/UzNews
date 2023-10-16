from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from rest_framework.test import APITestCase

from apps.common.models import Tag
from apps.interview.choices import InterviewStyleStatusChoices, StatusChoices
from apps.interview.models import Interview, Comment
from apps.users.models import User


class InterviewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            password="test_password",
            phone_number="+998901234567",
            first_name="test_user",
        )
        self.interview = Interview.objects.create(
            author=self.user,
            title="Intervire Title",
            style_type=InterviewStyleStatusChoices.STYLE_1,
            status=StatusChoices.DRAFT,
            subtitle="Subtitle Test",
            video_url="https://www.figma.com/file/",
        )
        self.uploaded_file_png = SimpleUploadedFile("cover.jpg", b"file_content", content_type="image/jpeg")

        self.tag = Tag.objects.create(name="Tag 1")
        self.comment = Comment.objects.create(
            interview=self.interview,
            user=self.user,
            text='Comment Text',
            image=self.uploaded_file_png
        )

    def test_interview_list(self):
        url = reverse("interview-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 1)

    def test_interview_detail(self):
        url = reverse(
            "interview-detail",
            kwargs={"pk": self.interview.id},
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Interview.objects.count(), 1)

    def test_interview_comment_list(self):
        url = reverse("interview_comments")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 1)

    def test_interview_comment_create(self):
        url = reverse('interview_comment_create', kwargs={
            "slug": self.interview.slug
        })
        data = {
            "text": "Comment Text",
            "user" : self.user
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 2001)
        self.assertEqual(response.data["count"], 1)

