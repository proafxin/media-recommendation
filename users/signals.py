from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import User, Profile

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    user = instance
    if created:
        profile = Profile(user=user)
        profile.save()
    instance.profile.save()