"""
Author: Masum Billal
Define models for keeping history of media-user
"""

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Creator(models.Model):
    """
    model class for the entity 'creator'
    contains creator related information
    """

    name = models.CharField(max_length=50)
    genre = models.IntegerField(
        max_length=1,
        choices=settings.CREATOR_TYPES,
    )


class Media(models.Model):
    """
    model class for the entity 'media'
    contains media related information
    """

    title = models.CharField(max_length=50)
    genre = models.IntegerField(
        max_length=1,
        choices=settings.MEDIA_TYPES,
    )
    creator = models.ForeignKey(
        Creator,
        on_delete=models.CASCADE,
    )


class History(models.Model):
    """
    model class for the entity 'history'
    contains the history of a user viewing/rating a media
    """

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    media = models.ForeignKey(
        Media,
        on_delete=models.CASCADE,
    )
    views = models.IntegerField(max_length=10)
    rating = models.IntegerField(
        max_length=2,
        choices=settings.RATINGS,
    )
