from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

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

