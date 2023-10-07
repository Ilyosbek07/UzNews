from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel, LikeBase, NewsBase
from apps.users.models import Profile


class InterviewTag(BaseModel):
    name = models.CharField(_("Name"), max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Interview Tag"
        verbose_name_plural = "Interview Tags"


class Interview(BaseModel, NewsBase):
    tag = models.ManyToManyField(InterviewTag, related_name="interview_tag", verbose_name=_("Tag"))
    subtitle = models.CharField(_("Subtitle"), max_length=255)
    video_url = models.URLField(verbose_name=_("Video Url"))
    is_main = models.BooleanField(_("Is Main"), default=False)

    def __str__(self):
        return self.subtitle

    class Meta:
        verbose_name = "Interview"
        verbose_name_plural = "Interviews"


class InterviewLike(LikeBase, BaseModel):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="interview_user_like", verbose_name=_("Profile")
    )
    content = models.ForeignKey(
        Interview, on_delete=models.CASCADE, related_name="interview_like", verbose_name=_("Interview")
    )

    class Meta:
        verbose_name = _("User Interview Like")
        verbose_name_plural = _("User Interview Likes")
