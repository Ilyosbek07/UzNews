from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel, NewsBase


class StatusChoices(models.TextChoices):
    PUBLISHED = "published", _("Published")
    IN_MODERATION = "in_moderation", _("In Moderation")
    DRAFT = "draft", _("Draft")


class Tag(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Name"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")


class PhotoReport(NewsBase, BaseModel):
    subtitle = models.CharField(max_length=255, null=True, verbose_name=_("Subtitle"))
    tag = models.ManyToManyField("photoreport.Tag", null=True, verbose_name=_("Tags"))
    status = models.CharField(
        max_length=16,
        choices=StatusChoices.choices,
        null=True,
        verbose_name=_("Status"),
    )
    author = models.ForeignKey("users.User", on_delete=models.SET_NULL, null=True, verbose_name=_("Author"))
    liked = models.IntegerField(default=0, verbose_name=_("Liked"))
    views = models.IntegerField(default=0, verbose_name=_("Views"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Photo Report")
        verbose_name_plural = _("Photo Reports")


class PhotoReportLiked(BaseModel):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="photo_report_liked",
        verbose_name=_("User"),
    )
    photo_report = models.ForeignKey(
        PhotoReport,
        on_delete=models.CASCADE,
        related_name="photo_report_liked",
        verbose_name=_("Photo report"),
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        self.photo_report.liked += 1
        self.photo_report.save()

    class Meta:
        verbose_name = _("Photo report like")
        verbose_name_plural = _("Photo report likes")
        unique_together = ("user", "photo_report")


class PhotoReportView(BaseModel):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="photo_report_view",
        verbose_name=_("User"),
    )
    photo_report = models.ForeignKey(
        PhotoReport,
        on_delete=models.CASCADE,
        related_name="photo_report_view",
        verbose_name=_("Photo report"),
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        self.photo_report.views += 1
        self.photo_report.save()

    class Meta:
        verbose_name = _("Photo report view")
        verbose_name_plural = _("Photo report views")
        unique_together = ("user", "photo_report")


class GalleryImage(BaseModel):
    photo_report = models.ForeignKey(
        PhotoReport,
        on_delete=models.CASCADE,
        related_name=("gallery_image"),
        verbose_name=_("Photo report"),
    )
    image = models.ImageField(upload_to="photoreport/gallery_images", verbose_name=_("Image"))
    order = models.PositiveIntegerField(null=True, blank=True, verbose_name=_("Order"))
    is_main = models.BooleanField(default=False, verbose_name=_("Is Main"))

    def __str__(self):
        return f"Gallery Image {self.id}"

    class Meta:
        verbose_name = _("Gallery Image")
        verbose_name_plural = _("Gallery Images")


class Comment(BaseModel):
    photo_report = models.ForeignKey(PhotoReport, on_delete=models.CASCADE, verbose_name=_("Photo Report"))
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="comment",
        verbose_name=_("User"),
    )
    image = models.ImageField(
        upload_to="photoreport/comment_images",
        blank=True,
        null=True,
        verbose_name=_("Image"),
    )
    parent = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name=_("Parent Comment"),
    )
    text = models.TextField(null=True, blank=True, verbose_name=_("Text"))
    liked = models.IntegerField(default=0, verbose_name=_("Liked"))

    def __str__(self):
        return f"Comment by {self.user.username} on {self.photo_report.title}"

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")


class CommentLike(BaseModel):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="comment_like",
        verbose_name=_("User"),
    )
    comment = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
        related_name="comment_like",
        verbose_name=_("Comment"),
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        self.comment.liked += 1
        self.comment.save()

    class Meta:
        verbose_name = _("Comment like")
        verbose_name_plural = _("Comment likes")
        unique_together = ("user", "comment")
