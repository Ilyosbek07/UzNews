from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class StatusChoices(TextChoices):
    PUBLISHED = "published", _("Published")
    IN_MODERATION = "in_moderation", _("In Moderation")
    DRAFT = "draft", _("Draft")


class LikeStatusChoices(TextChoices):
    LIKED = "l", _("Liked")
    DISLIKED = "d", _("Disliked")
    NEUTRAL = "n", _("Neutral")


class InterviewStyleStatusChoices(TextChoices):
    STYLE_1 = "Style 1", _("Style 1")
    STYLE_2 = "Style 2", _("Style 2")
    STYLE_3 = "Style 3", _("Style 3")
