from django.db import models


class NewsPositionChoices(models.TextChoices):
    MAIN = "main", "Main"
    PRIME = "prime", "Prime"
    ORDINARY = "ordinary", "Ordinary"


class NewsStatusChoices(models.TextChoices):
    DRAFT = "draft", "Draft"
    IN_MODERATION = "in moderation", "In moderation"
    PUBLISHED = "published", "Published"


class NewsTypeChoices(models.TextChoices):
    SPECIAL = "special report", "Special Report"
    NEWS = "news", "News"
