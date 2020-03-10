from django.contrib import admin
from .models import Actor, Director, Writer, Singer

admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Writer)
admin.site.register(Singer)