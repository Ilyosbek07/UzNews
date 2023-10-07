from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class LikeStatusChoices(TextChoices):
    LIKED = "l", _("Liked")
    DISLIKED = "d", _("Disliked")
    NEUTRAL = "n", _("Neutral")


class InterviewStyleStatusChoices(TextChoices):
    style_1 = "Style 1", _("Style 1")
    style_2 = "Style 2", _("Style 2")
    style_3 = "Style 3", _("Style 3")
