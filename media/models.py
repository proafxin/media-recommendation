from django.db import models
from artist.models import Writer, Director, Actor, Singer

MEDIA_TYPES = [
    (1, 'Music'),
    (2, 'Movie'),
    (3, 'Video'),
    (4, 'Series'),
    (5, 'Games'),
]

class Album(models.Model):
    name = models.CharField(max_length=100)
    artists = models.ManyToManyField(Singer)

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    media_type = models.IntegerField(
        choices=MEDIA_TYPES,
        default=1,
    )
    homepage = models.URLField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class Media(models.Model):
    title = models.CharField(max_length=100)
    media_type = models.IntegerField(
        choices=MEDIA_TYPES,
        default=1,
    )
    rating = models.DecimalField(decimal_places=1, max_digits=2)
    popularity = models.IntegerField()
    rated_by = models.IntegerField()
    year = models.IntegerField()
    release_date = models.DateField()
    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    external_url = models.URLField(max_length=100, blank=True)

    def __str__(self):
        if self.media_type == 1:
            return self.title+' '+self

class Song(Media):
    writers = models.ManyToManyField(Writer)
    singers = models.ManyToManyField(Singer)
    album = models.ForeignKey(
        Album, 
        on_delete=models.CASCADE,
        null=True,
    )
    pass

class Video(Media):
    cast = models.ManyToManyField(Actor)
    director = models.ManyToManyField(Director)
    length = models.DecimalField(max_digits=6, decimal_places=2)
    pass

class Game(Media):
    pass

class Series(Media):
    cast = models.ManyToManyField(Actor)
    director = models.ManyToManyField(Director)
    writers = models.ManyToManyField(Writer)
    num_seasons = models.IntegerField()
    num_episodes = models.IntegerField()
    max_episode_length = models.DecimalField(
        max_digits=6,
        decimal_places=2,
    )
    pass

class Movie(Media):
    cast = models.ManyToManyField(Actor)
    director = models.ManyToManyField(Director)
    writers = models.ManyToManyField(Writer)
    length = models.DecimalField(max_digits=6, decimal_places=2)
    pass