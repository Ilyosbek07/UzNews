from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator

from apps.users.models import Profile
from apps.common.models import BaseModel, NewsBase
from .choices import PreferenceStatusChoices

class Tag(BaseModel):
    name = models.CharField(_("Name"), max_length=100)

    class Meta:
        verbose_name = _("Podcast Tag")
        verbose_name_plural = _("Podcast Tags")

    def __str__(self):
        return self.name
    

class Category(BaseModel):
    name = models.CharField(_("Name"), max_length=100)
    slug = models.SlugField(_("Slug"))
    icon = models.FileField(_("Icon"), upload_to="podcast/icons/")

    class Meta:
        verbose_name = _("Podcast Category")
        verbose_name_plural = _("Podcast Categories")

    def __str__(self):
        return self.name
    

class Podcast(BaseModel, NewsBase):
    view_count = models.PositiveIntegerField(_("View count"), default=0)
    like_count = models.PositiveIntegerField(_("Like count"), default=0)
    dislike_count = models.PositiveSmallIntegerField(_("Dislike count"), default=0)
    cover = models.ImageField(
        _("Cover"), upload_to='podcast/covers/', 
        default='default_podcast_cover.png'
    )
    file = models.FileField(
        _("File"), upload_to='podcast/audios/',
        validators=[FileExtensionValidator(
            allowed_extensions=["mp3", "mp4a", "wav"]
        )] 
    )
    tags = models.ManyToManyField(
        Tag, verbose_name=_("Tags"), 
        related_name="podcasts"
    )
    author = models.ForeignKey(
        Profile,
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name="podcasts",
        verbose_name=_("Author")
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="podcasts",
        verbose_name=_("Category")
    )

    class Meta:
        verbose_name = _("Podcast")
        verbose_name_plural = _("Podcasts")

    def __str__(self):
        return self.title


class UserPreferenceBaseModel(models.Model):
    status = models.CharField(
        _('Status'), max_length=1,
        choices=PreferenceStatusChoices.choices,
        default=PreferenceStatusChoices.NEUTRAL
    )
    profile = None
    content = None

    class Meta:
        unique_together = ['profile', 'content']
        abstract = True

    def __str__(self):
        return f"{self.profile.__str__()}: {self.content.__str__()}"


class UserPodcastPreference(BaseModel, UserPreferenceBaseModel):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="podcast_preferences",
        verbose_name=_("Profile")
    )
    content = models.ForeignKey(
        Podcast,
        on_delete=models.CASCADE,
        related_name="user_preferences",
        verbose_name=_("Podcast")
    )

    class Meta:
        verbose_name = _("User Podcast Preference")
        verbose_name_plural = _("User Podcast Preferences")
