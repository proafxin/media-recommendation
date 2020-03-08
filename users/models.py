from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    date_of_birth = models.DateField()
    gender = models.CharField(
        choices=settings.GENDERS,
        max_length=1,
    )

    REQUIRED_FIELDS = [
        'email',
        'date_of_birth',
    ]

    def __str__(self):
        return self.first_name+' '+self.last_name