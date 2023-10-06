from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class LikeStatusChoices(TextChoices):
    LIKED = "l", _("Liked")
    DISLIKED = "d", _("Disliked")
    NEUTRAL = "n", _("Neutral")