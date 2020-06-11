from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

class User(AbstractUser):
    date_of_birth = models.DateField()
    gender = models.IntegerField(
        choices=settings.GENDERS,
    )

    REQUIRED_FIELDS = [
        'first_name',
        'last_name',
        'email',
        'date_of_birth',
        #'gender',
    ]

    def __str__(self):
        return self.first_name+' '+self.last_name

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    date_of_birth = models.DateField()


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()