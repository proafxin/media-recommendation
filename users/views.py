from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

class Home(TemplateView):
    template_name = 'users/home.html'