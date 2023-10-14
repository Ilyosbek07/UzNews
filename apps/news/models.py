from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from apps.common.models import (BaseModel, ContentLike, ContentView, NewsBase,
                                Tag)
from apps.news.choices import (NewsPositionChoices, NewsStatusChoices,
                               NewsStyleChoices, NewsTypeChoices)
from apps.news.managers import NewsManager
from apps.users.models import User


class NewsCategory(models.Model):
    name = models.CharField(_("name of category"), max_length=255)

    def __str__(self):
        return self.name


class News(NewsBase, BaseModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author_to_news")
    is_verified = models.BooleanField(blank=True)
    cover = models.ImageField(upload_to="news/cover_images/")
    tags = models.ManyToManyField(Tag, related_name="news_to_tags")
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)
    position = models.CharField(
        _("position of news in main site page"),
        max_length=100,
        choices=NewsPositionChoices.choices,
        default=NewsPositionChoices.ORDINARY,
    )
    status = models.CharField(
        max_length=100,
        choices=NewsStatusChoices.choices,
        default=NewsStatusChoices.DRAFT,
    )
    type = models.CharField(max_length=100, choices=NewsTypeChoices.choices, default=NewsTypeChoices.NEWS)
    style = models.CharField(
        _("news appearing style in site"),
        max_length=100,
        choices=NewsStyleChoices.choices,
        default=NewsStyleChoices.STYLE_1,
    )
    objects = NewsManager()

    class Meta:
        verbose_name_plural = "News"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

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

    @property
    def view_count(self):
        return ContentView.objects.filter(news__id=self.id).count()


class NewsCancelReason(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    text = models.TextField(_("the reason of cancel"))


class BreakingNews(BaseModel):
    title = models.CharField(max_length=1200)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    expire_time = models.DateTimeField()

    class Meta:
        unique_together = ("id", "news")
        verbose_name_plural = "BreakingNews"

    def __str__(self):
        return self.title
