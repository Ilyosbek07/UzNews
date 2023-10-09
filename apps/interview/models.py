from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel, LikeBase, NewsBase
from apps.interview.choices import InterviewStyleStatusChoices, StatusChoices
from apps.users.models import Profile, User


class InterviewTag(BaseModel):
    name = models.CharField(_("Name"), max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Interview Tag"
        verbose_name_plural = "Interview Tags"


class Interview(BaseModel, NewsBase):
    like_count = models.PositiveIntegerField(_("Like count"), default=0)
    dislike_count = models.PositiveSmallIntegerField(_("Dislike count"), default=0)
    style_type = models.CharField(
        max_length=55,
        choices=InterviewStyleStatusChoices.choices,
        verbose_name=_("Style Type"),
        default=InterviewStyleStatusChoices.STYLE_1
    )
    status = models.CharField(
        max_length=55,
        choices=StatusChoices.choices,
        verbose_name=_("Status"),
        default=StatusChoices.DRAFT
    )
    tag = models.ManyToManyField(InterviewTag, related_name="interview_tag", verbose_name=_("Tag"))
    subtitle = models.CharField(verbose_name=_("Subtitle"), max_length=255)
    video_url = models.URLField(verbose_name=_("Video Url"))
    is_main = models.BooleanField(verbose_name=_("Is Main"), default=False)

    def __str__(self):
        return self.subtitle

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Interview"
        verbose_name_plural = "Interviews"


class InterviewLike(LikeBase, BaseModel):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="interview_user_like", verbose_name=_("User")
    )
    content = models.ForeignKey(
        Interview, on_delete=models.CASCADE, related_name="interview_like", verbose_name=_("Interview")
    )

    class Meta:
        verbose_name = _("User Interview Like")
        verbose_name_plural = _("User Interview Likes")


class InterviewView(BaseModel):
    interview = models.ForeignKey(
        Interview,
        verbose_name=_("Interview"),
        on_delete=models.CASCADE,
        related_name="interview_view",
    )
    user = models.ForeignKey(
        User,
        verbose_name=_("User"),
        on_delete=models.CASCADE,
        related_name="user_views",
        null=True,
        blank=True,
    )
    device_id = models.CharField(
        verbose_name=_("Identified device"),
        max_length=255,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = _("Interview View")
        verbose_name_plural = _("Interview Views")
