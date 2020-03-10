from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    height = models.DecimalField(decimal_places=1, max_digits=5)
    bio = models.TextField(max_length=500)

    def __str__(self):
        return self.name

class Director(Artist):
    pass

class Writer(Artist):
    pass

class Actor(Artist):
    pass

class Singer(Artist):
    pass