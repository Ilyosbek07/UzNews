from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class Advertising_choices(TextChoices):
    banner = "banner", _("Banner")
    banner2 = "banner2", _("Banner 2")
    pr_article = "pr_article", _("Pr Article")
    full_screen = "full_screen", _("Full Screen")


class LikeStatusChoices(TextChoices):
    LIKED = "l", _("Liked")
    DISLIKED = "d", _("Disliked")
    NEUTRAL = "n", _("Neutral")
