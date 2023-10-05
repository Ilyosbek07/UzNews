from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from apps.users.models import Profile, User


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_delete, sender=Profile)
def delete_user_when_deleted_profile(sender, instance, **kwargs):
    instance.user.delete()
