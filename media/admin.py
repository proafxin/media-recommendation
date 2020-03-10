from django.contrib import admin
from .models import (
    Song, 
    Video, 
    Movie, 
    Series, 
    Game, 
    Publisher, 
    Album,
    Band,
)


admin.site.register(Song)
admin.site.register(Video)
admin.site.register(Movie)
admin.site.register(Series)
admin.site.register(Game)
admin.site.register(Publisher)
admin.site.register(Album)
admin.site.register(Band)