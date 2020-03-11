from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
)
from .models import (
    Actor,
    Singer,
    Writer,
    Director,
)

class ActorListView(ListView):
    model = Actor

class SingerListView(ListView):
    model = Singer

class SingerDetailView(DetailView):
    model = Singer

class WriterListView(ListView):
    model = Writer

class DirectorListView(ListView):
    model = Director