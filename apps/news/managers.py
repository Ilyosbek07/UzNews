from django.db import models


class NewsManager(models.Manager):
    def published(self):
        return self.filter(status="published")
