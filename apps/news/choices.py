from django.db import models


class NewsPositionChoices(models.TextChoices):
    MAIN = "main", "Main"
    PRIME = "prime", "Prime"
    ORDINARY = "ordinary", "Ordinary"


class NewsStyleChoices(models.TextChoices):
    STYLE_1 = "style 1", "Style 1"
    STYLE_2 = "style 2", "Style 2"


class NewsStatusChoices(models.TextChoices):
    DRAFT = "draft", "Draft"
    IN_MODERATION = "in moderation", "In moderation"
    PUBLISHED = "published", "Published"


class NewsTypeChoices(models.TextChoices):
    ARTICLE = "article", "Article"
    NEWS = "news", "News"
