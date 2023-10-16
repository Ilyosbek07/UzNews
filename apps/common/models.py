from ckeditor.fields import RichTextField
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from apps.common.choices import Advertising_choices, ContentChoices, LikeStatusChoices
from apps.users.models import User

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


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
            time_difference_in_seconds = (timezone.now() - self.created_at).total_seconds()
            if 3600 > int(time_difference_in_seconds) > 60:
                data["minute"] = int((int(time_difference_in_seconds) / 60))
            elif 86400 >= int(time_difference_in_seconds) >= 3600:
                data["hour"] = int(time_difference_in_seconds / 3600)
            else:
                data["today"] = self.created_at.strftime("%H:%M")
        return data or self.created_at

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
    type = models.CharField(
        max_length=55, choices=Advertising_choices.choices, default=Advertising_choices.banner, verbose_name=_("Type")
    )

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


class Category(BaseModel):
    name = models.CharField(_("Name"), max_length=100)
    slug = models.SlugField(_("Slug"))
    icon = models.FileField(_("Icon"), upload_to="podcast/icons/")

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name


class Tag(BaseModel):
    name = models.CharField(_("Name"), max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"


class CountViewManager(models.Manager):
    def create_for_object(self, obj, user, device_id):
        content_type = ContentType.objects.get_for_model(obj)
        return self.create(
            content_type=content_type, object_id=obj.id, user=user, device_id=device_id
        )


class ContentView(BaseModel):
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        verbose_name=_("Content view"),
        related_name="%(app_label)s_%(class)s_related",
        null=True,
        blank=True,
    )
    object_id = models.PositiveIntegerField(verbose_name=_("Object id"))
    content_object = GenericForeignKey("content_type", "object_id")
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="%(app_label)s_%(class)s_related",
        verbose_name=_("User"),
    )
    device_id = models.CharField(
        verbose_name=_("Identified device"),
        max_length=255,
        null=True,
        blank=True,
    )

    objects = CountViewManager()

    def str(self):
        return f"{self.content_type}"

    class Meta:
        unique_together = (
            ("content_type", "object_id", "user"),
            ("content_type", "object_id", "device_id"),
        )


class CountLikeManager(models.Manager):
    def create_for_object(self, obj, user, status):
        content_type = ContentType.objects.get_for_model(obj)
        return self.create(
            content_type=content_type, object_id=obj.id, user=user, status=status
        )


class ContentLike(BaseModel):
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        related_name="content_like",
        verbose_name=_("Content like"),
        null=True,
        blank=True,
    )
    object_id = models.PositiveIntegerField(verbose_name=_("Object id"))
    content_object = GenericForeignKey("content_type", "object_id")
    status = models.CharField(
        max_length=10, choices=LikeStatusChoices.choices, verbose_name=_("Like status")
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="content_like_user",
        verbose_name=_("User"),
    )

    objects = CountLikeManager()

    def __str__(self):
        return f"{self.content_type}"

    class Meta:
        unique_together = ("content_type", "object_id", "user")


class CountReportManager(models.Manager):
    def create_for_object(self, obj, user, status):
        content_type = ContentType.objects.get_for_model(obj)
        return self.create(
            content_type=content_type, object_id=obj.id, user=user, status=status
        )


class ContentReport(BaseModel):
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        related_name="content_comment_user",
        verbose_name=_("Content Report"),
        null=True,
        blank=True,
    )
    object_id = models.PositiveIntegerField(verbose_name=_("Object id"))
    content_object = GenericForeignKey("content_type", "object_id")
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="content_report",
        verbose_name=_("User"),
    )

    objects = CountLikeManager()

    def __str__(self):
        return f"{self.content_type}"

    class Meta:
        unique_together = ("content_type", "object_id", "user")


class CountCommentManager(models.Manager):
    def create_for_object(self, obj, user, status):
        content_type = ContentType.objects.get_for_model(obj)
        return self.create(
            content_type=content_type, object_id=obj.id, user=user, status=status
        )


class ContentComment(BaseModel):
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        related_name="content_comment",
        verbose_name=_("Content comment"),
        null=True,
        blank=True,
    )
    object_id = models.PositiveIntegerField(verbose_name=_("Object id"))
    content_object = GenericForeignKey("content_type", "object_id")
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="content_comment_user",
        verbose_name=_("User"),
    )

    objects = CountLikeManager()

    def __str__(self):
        return f"{self.content_type}"

    class Meta:
        unique_together = ("content_type", "object_id", "user")
