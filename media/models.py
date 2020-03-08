from django.db import models
from artist.models import Writer, Director, Actor

MEDIA_TYPES = [
    (1, 'Music'),
    (2, 'Movie'),
    (3, 'Video'),
    (4, 'Series'),
    (5, 'Games'),
]

class Media(models.Model):
    title = models.CharField(max_length=100)
    media_type = models.IntegerField(
        choices=MEDIA_TYPES,
        default=1,
    )
    director = models.ManyToManyField(Director)
    writer = models.ManyToManyField(Writer)
    actor = models.ManyToManyField(Actor)
    rating = models.DecimalField(decimal_places=1, max_digits=2)
    popularity = models.IntegerField()
    rated_by = models.IntegerField()
    year = models.IntegerField()
    release_date = models.DateField()

    def __str__(self):
        if self.media_type == 1:
            return self.title+' '+self