"""
Author: Masum Billal
Write views to be mapped to urls
"""

from django.conf import settings
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from recommender_api.models import (
    Creator,
    # Media,
    # History,
)
from recommender_api.serializers import (
    CreatorSerializer,
)


class CreatorList(ListCreateAPIView):
    """
    view for creating new creator on post request
    and list of creators on get request
    """

    queryset = Creator.objects.all()
    serializer_class = CreatorSerializer
    authentication_classes = settings.AUTHENTICATION_CLASSES
    permission_classes = settings.PERMISSION_CLASSES

class CreatorGeneric(RetrieveUpdateDestroyAPIView):
    """
    generic view to get, put, delete 'creator'
    """

    queryset = Creator.objects.all()
    serializer_class = Creator
    authentication_classes = settings.AUTHENTICATION_CLASSES
    permission_classes = settings.PERMISSION_CLASSES
