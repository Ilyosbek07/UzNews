# from django.core.files.uploadedfile import SimpleUploadedFile
# from django.urls import reverse
# from rest_framework.test import APITestCase
#
# from apps.common.models import Tag
# from apps.interview.choices import StatusChoices, InterviewStyleStatusChoices
# from apps.interview.models import Interview
# from apps.podcast.choices import PodcastStatusChoices
# from apps.podcast.models import Podcast
# from apps.users.models import Profile, User
#
#
# class BackOfficePodcastTestCase(APITestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(
#             phone_number='+998935036638',
#             password='new_pass'
#         )
#         self.profile = Profile.objects.create(
#             user=self.user,
#             info='User info',
#         )
#         self.tag = Tag.objects.create(name="Tag 1")
#         self.uploaded_file_png = SimpleUploadedFile(
#             "test_file.png",
#             b"Test content for the file",
#             content_type="text/plain"
#         )
#         self.uploaded_file_mp3 = SimpleUploadedFile(
#             "test_file.mp3",
#             b"Test content for the file",
#             content_type="text/plain"
#         )
#         self.podcast = Podcast.objects.create(
#             title="Title",
#             status=PodcastStatusChoices.DRAFT,
#             subtitle="Subtitle Test",
#             body="<h1>Title</h1>",
#             cover=self.uploaded_file_png,
#             file=self.uploaded_file_mp3,
#             author=self.profile,
#             tags=[self.tag]
#         )
#
#     def test_podcast_list(self):
#         url = reverse("back_podcast_list")
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.data["count"], 1)

# def test_podcast_create(self):
#     url = reverse("back_podcast_create")
#     data = {
#         "title": "New Interview",
#         "subtitle": "New Subtitle",
#         "status": PodcastStatusChoices.DRAFT,
#         "tag": [self.tag.id],
#     }
#     response = self.client.post(url, data=data)
#     self.assertEqual(response.status_code, 201)
#     self.assertEqual(Interview.objects.count(), 2)
#
# def test_interview_detail(self):
#     url = reverse(
#         "back_interview_detail",
#         kwargs={"pk": self.interview.id},
#     )
#     response = self.client.get(url)
#     self.assertEqual(response.status_code, 200)
#     self.assertEqual(Interview.objects.count(), 1)
#
# def test_interview_put(self):
#     url = reverse(
#         "back_interview_update",
#         kwargs={"pk": self.interview.id},
#     )
#     data = {
#         "title": "New Title",
#         "subtitle": "New Sub Title",
#         "status": "published",
#         "video_url": "http://127.0.0.1:8080/swagger/",
#         "tag": [self.tag.id],
#     }
#     response = self.client.put(url, data=data)
#     self.assertEqual(response.status_code, 200)
#     self.assertEqual(response.data["title"], "New Title")
#     self.assertEqual(response.data["subtitle"], "New Sub Title")
#
# def test_interview_patch(self):
#     url = reverse(
#         "back_interview_update",
#         kwargs={"pk": self.interview.id},
#     )
#     data = {"title": "New Title"}
#     response = self.client.patch(url, data=data)
#     self.assertEqual(response.status_code, 200)
#     self.assertEqual(response.data["title"], "New Title")
#
# def test_interview_delete(self):
#     url = reverse(
#         "back_interview_delete",
#         kwargs={"pk": self.interview.id},
#     )
#     response = self.client.delete(url)
#     self.assertEqual(response.status_code, 204)
#     self.assertEqual(Interview.objects.count(), 0)
