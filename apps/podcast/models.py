from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.contenttypes.models import ContentType
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from apps.common.choices import LikeStatusChoices
from apps.common.models import BaseModel, ContentLike, ContentView
from apps.users.models import Profile

from .choices import PodcastStatusChoices


class Tag(BaseModel):
    name = models.CharField(_("Name"), max_length=255)

    def __str__(self):
        return self.name


class Category(BaseModel):
    name = models.CharField(_("Name"), max_length=100)
    slug = models.SlugField(_("Slug"), blank=True)
    icon = models.FileField(_("Icon"), upload_to="podcast/icons/")

    class Meta:
        verbose_name = _("Podcast Category")
        verbose_name_plural = _("Podcast Categories")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Podcast(BaseModel):
    title = models.CharField(_("Title"), max_length=255)
    slug = models.SlugField(_("Slug"), blank=True)
    subtitle = models.CharField(_("Subtitle"), max_length=255)
    body = RichTextUploadingField(_("Body"))
    status = models.CharField(_("Status"), max_length=2, choices=PodcastStatusChoices.choices)
    cover = models.ImageField(_("Cover"), upload_to="podcast/covers/", default="default_podcast_cover.png")
    file = models.FileField(
        _("File"),
        upload_to="podcast/audios/",
        validators=[FileExtensionValidator(allowed_extensions=["mp3", "mp4a", "wav"])],
    )
    tags = models.ManyToManyField(Tag, verbose_name=_("Tags"), related_name="podcasts")
    author = models.ForeignKey(
        Profile,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="podcasts",
        verbose_name=_("Author"),
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="podcasts",
        verbose_name=_("Category"),
    )

    class Meta:
        verbose_name = _("Podcast")
        verbose_name_plural = _("Podcasts")

    def get_view_count(self):
        return ContentView.objects.filter(
            content_type=ContentType.objects.get_for_model(Podcast), object_id=self.id
        ).count()

    def get_like_dislike_count(self):
        like_dislike = ContentLike.objects.filter(
            content_type=ContentType.objects.get_for_model(Podcast), object_id=self.id
        )
        like_count = like_dislike.filter(status=LikeStatusChoices.LIKED).count()
        dislike_count = like_dislike.filter(status=LikeStatusChoices.DISLIKED).count()
        return {"like": like_count, "dislike": dislike_count}

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Comment(BaseModel):
    text = models.TextField(_("Text"), max_length=400)
    is_active = models.BooleanField(_("Is active"), default=True)
    image = models.ImageField(_("Image"), upload_to="podcast/comments/", null=True, blank=True)
    profile = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="podcast_comments",
        verbose_name=_("Owner"),
    )
    podcast = models.ForeignKey(
        Podcast,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name=_("Podcast"),
    )
    parent = models.ForeignKey(
        to="self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="replies",
        verbose_name=_("Parent"),
    )

    class Meta:
        verbose_name = _("Podcast Comment")
        verbose_name_plural = _("Podcast Comments")

    def get_like_dislike_count(self):
        like_dislike = ContentLike.objects.filter(
            content_type=ContentType.objects.get_for_model(Comment), object_id=self.id
        )
        like_count = like_dislike.filter(status=LikeStatusChoices.LIKED).count()
        dislike_count = like_dislike.filter(status=LikeStatusChoices.DISLIKED).count()
        return {"like": like_count, "dislike": dislike_count, "total": like_count + dislike_count}

    def __str__(self):
        return self.text


class CommentComplaint(BaseModel):
    text = models.TextField(_("Text"), max_length=400)
    profile = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="podcast_comment_complaints",
        verbose_name=_("Owner"),
    )
    comment = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
        related_name="complaints",
        verbose_name=_("Comment"),
    )

    class Meta:
        verbose_name = _("Podcast Comment Complaint")
        verbose_name_plural = _("Podcast Comment Complaints")

    def __str__(self):
        return self.text
