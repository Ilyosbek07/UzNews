from django.db import models
from django.utils.translation import gettext_lazy as _


class Role(models.TextChoices):
    simple_user = "simple user", _("Simple User")
    author = "author", _("Author")
    moderator = "moderator", _("Moderator")
