from django.utils.text import slugify

from apps.users.models import User
from django.db import models
from apps.common.models import NewsBase, BaseModel, LikeBase, CommentBase, ReportBase
from apps.news.choices import NewsPositionChoices, NewsTypeChoices, NewsStatusChoices
from apps.news.managers import NewsManager


class NewsTag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "News Tags"


class NewsCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class News(NewsBase, BaseModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    cover = models.ImageField(upload_to="news/cover_images/")
    tag = models.ManyToManyField(NewsTag)
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)
    position = models.CharField(
        max_length=100,
        choices=NewsPositionChoices.choices,
        default=NewsPositionChoices.ORDINARY,
    )
    status = models.CharField(
        max_length=100,
        choices=NewsStatusChoices.choices,
        default=NewsStatusChoices.DRAFT,
    )
    type = models.CharField(
        max_length=100, choices=NewsTypeChoices.choices, default=NewsTypeChoices.NEWS
    )
    objects = NewsManager()

    class Meta:
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    @property
    def view_count(self):
        return NewsView.objects.filter(news__id=self.id).count()
        

class NewsLike(LikeBase):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)

    def __str__(self):
        return self.news.title


class NewsComment(CommentBase, BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class NewsCommentReport(ReportBase, BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(NewsComment, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class NewsView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)

    def __str__(self):
        return self.news.title


class BreakingNews(BaseModel):
    title = models.CharField(max_length=1200)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    expire_time = models.DateTimeField()

    class Meta:
        unique_together = ("id", "news")
        verbose_name_plural = 'BreakingNews'

    def __str__(self):
        return self.title
