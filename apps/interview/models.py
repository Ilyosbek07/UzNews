from django.db import models
from apps.common.models import BaseModel, NewsBase, LikeBase
from django.utils.translation import gettext_lazy as _


class InterviewLike(LikeBase):
    pass


class InterviewTag(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Interview Tag"
        verbose_name_plural = "Interview Tags"


class Interview(BaseModel, NewsBase):
    tag = models.ManyToManyField(
        InterviewTag,
        related_name="interview_tag",
    )
    subtitle = models.CharField(max_length=255)
    video_url = models.URLField(verbose_name=_("Video Url"))
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return self.subtitle

    class Meta:
        verbose_name = "Interview"
        verbose_name_plural = "Interviews"
