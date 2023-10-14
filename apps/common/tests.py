from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from rest_framework import test

from apps.common.choices import Advertising_choices
from apps.common.models import Advertising, SocialMedia, Tag


class CommonAPITestCase(test.APITestCase):
    def setUp(self):
        self.file = SimpleUploadedFile("test_file.png", b"Test content for the file", content_type="text/plain")
        self.social_media = SocialMedia.objects.create(
            logo=self.file,
            url="http://127.0.0.1:8000/swagger/",
            number=1,
            desc="Description",
        )
        self.advertising = Advertising.objects.create(
            file=self.file,
            type=Advertising_choices.banner,
        )
        self.tag = Tag.objects.create(name="Tag 1")

    def test_get_social_media_list(self):
        url = reverse("social_media_list")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(SocialMedia.objects.count(), 1)

    def test_get_advertising_list(self):
        url = reverse("advertising_list")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(Advertising.objects.count(), 1)
