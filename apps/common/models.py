from ckeditor.fields import RichTextField
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from apps.common.choices import LikeStatusChoices


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class NewsBase(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    slug = models.SlugField(default="", null=False, verbose_name=_("Slug"))
    author = None
    desc = RichTextField(verbose_name=_("Description"), default="")
    created_at = None

    @property
    def date_time_in_word(self):
        data = dict()
        if self.created_at.date() == timezone.now().date():
            time_difference_in_seconds = (
                timezone.now() - self.created_at).total_seconds()
            if 3600 > int(time_difference_in_seconds) > 60:
                data["minute"] = int((int(time_difference_in_seconds) / 60))
            elif 86400 >= int(time_difference_in_seconds) >= 3600:
                data["hour"] = int(time_difference_in_seconds / 3600)
            else:
                data["today"] = self.created_at.strftime("%H:%M")
        return data or self.created_at

    class Meta:
        abstract = True


class CommentBase(models.Model):
    user = None
    text = models.TextField(verbose_name=_("Text"))
    is_active = models.BooleanField(default=False, verbose_name=_("Is Active"))
    parent = models.ForeignKey(
        "self",
        verbose_name=_("Parent"),
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_related",
    )
    image = models.ImageField(verbose_name=_("Image"))

    class Meta:
        abstract = True


class ReportBase(models.Model):
    text = models.CharField(max_length=255, verbose_name=_("Text"), null=True, blank=True)

    class Meta:
        abstract = True


class LikeBase(models.Model):
    user = None
    content = None
    status = models.CharField(max_length=10, choices=LikeStatusChoices.choices, verbose_name=_("Status"))

    class Meta:
        abstract = True


class ContactBase(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    phone_number = models.CharField(max_length=255, verbose_name=_("Phone Number"))
    text = models.TextField(verbose_name=_("Text"))

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")


class Advertising(models.Model):
    file = models.FileField(verbose_name=_("File"))
    Advertising_choices = [
        ("banner", _("Banner")),
        ("banner2", _("Banner 2")),
        ("pr_article", _("Pr Article")),
        ("full_screen", _("Full Screen")),
    ]
    type = models.CharField(max_length=55, choices=Advertising_choices, verbose_name=_("Type"))

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = _("Advertising")
        verbose_name_plural = _("Advertisements")


class SocialMedia(models.Model):
    logo = models.ImageField(verbose_name=_("Logo"))
    url = models.URLField(verbose_name=_("URL"))
    number = models.IntegerField(verbose_name=_("Number"))
    desc = models.TextField(verbose_name=_("Description"))

    def __str__(self):
        return f"Social media {self.id}"

    class Meta:
        verbose_name = _("Social Media")
        verbose_name_plural = _("Social Media")


class Tag(BaseModel):
    name = models.CharField(_("Name"), max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
