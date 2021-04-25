"""
Author: Masum Billal
Views for users API
"""

from django.contrib.auth.models import User
from django.conf import settings

from rest_framework.generics import (
    ListCreateAPIView,
)

from users.serializers import UserSerializer


class UserList(ListCreateAPIView):
    """
    Get endpoint for list of users
    and post endpoint to create new user
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = settings.AUTHENTICATION_CLASSES
    permission_classes = settings.PERMISSION_CLASSES
