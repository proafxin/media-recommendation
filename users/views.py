from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
)
from django.utils.decorators import (
    method_decorator,
)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User
from .forms import SignUpForm

class Home(TemplateView):
    template_name = 'users/home.html'

class Dashboard(TemplateView):
    template_name = 'users/home.html'

class Profile(DetailView):
    template_name = 'users/profile.html'

class SignUp(SuccessMessageMixin, CreateView):
    form_class = SignUpForm
    model = User
    template_name = 'users/signup.html'
    success_message = 'Your account was created successfully'
    success_url = '/signin'