from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel, NewsBase


class Category(BaseModel):
    name = models.CharField(_("Name"), max_length=100)
    slug = models.SlugField(_("Slug"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Review Category")
        verbose_name_plural = _("Review Categories")


class Review(NewsBase, BaseModel):
    subtitle = models.CharField(
        max_length=255, blank=True, null=True, verbose_name=_("Subtitle")
    )
    tag = models.ManyToManyField("common.Tag", blank=True, verbose_name=_("Tags"))
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name=_("Category"),
    )
    author = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="reviews",
        verbose_name=_("Author"),
    )
    image = models.ImageField(
        upload_to="review/images", blank=True, null=True, verbose_name=_("Image")
    )
    cover = models.ImageField(
        upload_to="review/covers", blank=True, null=True, verbose_name=_("Cover")
    )
    liked = models.IntegerField(default=0, verbose_name=_("Liked"))
    view = models.IntegerField(default=0, verbose_name=_("View"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Review")
        verbose_name_plural = _("Reviews")


class Comment(BaseModel):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name=_("Review"),
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name=_("User"),
    )
    image = models.ImageField(
        upload_to="comment/comment_images",
        blank=True,
        null=True,
        verbose_name=_("Image"),
    )
    parent = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="replies",
        verbose_name=_("Parent Comment"),
    )
    text = models.TextField(null=True, blank=True, verbose_name=_("Text"))
    liked = models.IntegerField(default=0, verbose_name=_("Liked"))

    def __str__(self):
        return f"Comment to {self.review.title}"

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")


class CommentLike(BaseModel):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="comment_likes",
        verbose_name=_("User"),
    )
    comment = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
        related_name="comment_likes",
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
