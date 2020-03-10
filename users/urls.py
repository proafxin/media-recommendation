from django.urls import path
from users.views import Home
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('signin/', LoginView.as_view(template_name='users/signin.html'), name='signin'),
    path('signout/', LogoutView.as_view(template_name='users/signout.html'), name='signout'),
]