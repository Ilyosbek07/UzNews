from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class PodcastStatusChoices(TextChoices):
    DRAFT = "dr", _("Draft")
    IN_MODERATION = "im", _("In moderation")
    PUBLISHED = "pb", _("Published")


class LikeStatusChoices(TextChoices):
    LIKED = "l", _("Liked")
    DISLIKED = "d", _("Disliked")
    NEUTRAL = "n", _("Neutral")
