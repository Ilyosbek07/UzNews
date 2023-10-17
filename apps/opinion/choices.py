from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class OpinionStatusChoices(TextChoices):
    DRAFT = "dr", _("Draft")
    IN_MODERATION = "im", _("In moderation")
    PUBLISHED = "pb", _("Published")
