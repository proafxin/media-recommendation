from django.db import models
from artist.models import Writer, Director, Actor, Singer

MEDIA_TYPES = [
    (1, 'Music'),
    (2, 'Movie'),
    (3, 'Video'),
    (4, 'Series'),
    (5, 'Games'),
]


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    media_type = models.IntegerField(
        choices=MEDIA_TYPES,
        default=1,
    )
    form_year = models.IntegerField(null=True)
    homepage = models.URLField(max_length=100, null=True)

    def __str__(self):
        return self.name

class Band(Publisher):
    media_type = 1
    pass

class Album(models.Model):
    name = models.CharField(max_length=100)
    artists = models.ManyToManyField(Singer)
    band = models.ForeignKey(Band, null=True, on_delete=models.CASCADE)
    length = models.CharField(null=True, max_length=5)

    def __str__(self):
        return self.name

class Media(models.Model):
    title = models.CharField(max_length=100)
    media_type = models.IntegerField(
        choices=MEDIA_TYPES,
        default=1,
    )
    genre = models.CharField(max_length=100, default='pop')
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
    length = models.CharField(max_length=5, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    external_url = models.URLField(max_length=100, null=True, blank=True)

    def __str__(self):
        if self.media_type == 1:
            return self.title+' by '+self.publisher.name

class Song(Media):
    writers = models.ManyToManyField(Writer)
    singers = models.ManyToManyField(Singer)
    album = models.ForeignKey(
        Album, 
        on_delete=models.CASCADE,
        null=True,
    )

class Video(Media):
    cast = models.ManyToManyField(Actor)
    director = models.ManyToManyField(Director)
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
    pass