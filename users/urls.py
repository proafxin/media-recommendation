from django.urls import path
from users.views import (
    Home,
    SignUp,
    Profile,
)
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
)

urlpatterns = [
    path('home/', Home.as_view(), name='home'),
    path('', Home.as_view(), name='home'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('profile/', Profile.as_view(), name='profile'),
    path('signin/', LoginView.as_view(template_name='users/signin.html'), name='signin'),
    path('signout/', LogoutView.as_view(template_name='users/signout.html'), name='signout'),
]