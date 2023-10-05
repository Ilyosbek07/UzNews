from django.db import models
from django.utils.translation import gettext_lazy as _

class NewsBase(models.Model):
    slug = models.CharField(max_length=255, verbose_name=_("Slug"))
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    author = None  # You can add the author field here
    desc = models.TextField(verbose_name=_("Description"))

    class Meta:
        verbose_name = _("News")
        verbose_name_plural = _("News")

class CommentBase(models.Model):
    user = None  # You can add the user field here
    text = models.TextField(verbose_name=_("Text"))
    is_active = models.BooleanField(default=False, verbose_name=_("Is Active"))
    parent = models.ForeignKey('self', verbose_name=_("Parent"), on_delete=models.CASCADE)
    image = models.ImageField(verbose_name=_("Image"))

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")

class SocialMediaBase(models.Model):
    logo = models.ImageField(verbose_name=_("Logo"))
    url = models.URLField(verbose_name=_("URL"))
    number = models.IntegerField(verbose_name=_("Number"))
    desc = models.TextField(verbose_name=_("Description"))

    class Meta:
        verbose_name = _("Social Media")
        verbose_name_plural = _("Social Media")

class ReportBase(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    text = models.CharField(max_length=255, verbose_name=_("Text"))

    class Meta:
        verbose_name = _("Report")
        verbose_name_plural = _("Reports")

class ContactBase(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    phone_number = models.CharField(max_length=255, verbose_name=_("Phone Number"))
    text = models.TextField(verbose_name=_("Text"))

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")

class LikeBase(models.Model):
    user = None  # You can add the user field here
    STATUS_CHOICES = [
        ('liked', _("Liked")),
        ('disliked', _("Disliked")),
        ('neutral', _("Neutral")),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, verbose_name=_("Status"))

    class Meta:
        verbose_name = _("Like")
        verbose_name_plural = _("Likes")

class AdvertisingBase(models.Model):
    file = models.FileField(verbose_name=_("File"))
    TYPE_CHOICES = [
        ('type1', _("Type 1")),
        ('type2', _("Type 2")),
        ('type3', _("Type 3")),
    ]
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, verbose_name=_("Type"))

    class Meta:
        verbose_name = _("Advertising")
        verbose_name_plural = _("Advertisements")


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
