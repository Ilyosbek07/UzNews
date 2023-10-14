from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Review
from apps.review.utils import cartoonify_image


@receiver(post_save, sender=Review)
def process_cover_image(sender, instance, **kwargs):
    if instance.cover:
        image_path = instance.cover.path
        output_path = instance.cover.name
        path = cartoonify_image(image_path, output_path)
        print(path)
        if instance.cover != path:
            instance.cover = path  # Update the cover field with the new path
            instance.save()
