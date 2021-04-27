"""
Author: Masum Billal
Write views to be mapped to urls
"""

from django.conf import settings

from rest_framework.filters import SearchFilter

from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from recommender_api.models import (
    Creator,
    Media,
    History,
)
from recommender_api.serializers import (
    CreatorSerializer,
    MediaSerializer,
    HistorySerializer,
)

class BaseListAPIView(ListAPIView):
    """
    Base generic class for list API
    """

    authentication_classes = settings.AUTHENTICATION_CLASSES
    permission_classes = settings.PERMISSION_CLASSES


class CreatorList(ListCreateAPIView):
    """
    view for creating new creator on post request
    and list of creators on get request
    """

    queryset = Creator.objects.all()
    serializer_class = CreatorSerializer
    authentication_classes = settings.AUTHENTICATION_CLASSES
    permission_classes = settings.PERMISSION_CLASSES
    filter_backends = [SearchFilter]
    search_fields = [
        'name',
        'genre',
    ]


class CreatorGeneric(RetrieveUpdateDestroyAPIView):
    """
    generic view to get, put, delete 'creator'
    """

    queryset = Creator.objects.all()
    serializer_class = CreatorSerializer
    authentication_classes = settings.AUTHENTICATION_CLASSES
    permission_classes = settings.PERMISSION_CLASSES


class MediaList(ListCreateAPIView):
    """
    view to get media list and post new media
    """

    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    authentication_classes = settings.AUTHENTICATION_CLASSES
    permission_classes = settings.PERMISSION_CLASSES


class MediaGeneric(RetrieveUpdateDestroyAPIView):
    """
    generic view to get, put, delete 'media'
    """

    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    authentication_classes = settings.AUTHENTICATION_CLASSES
    permission_classes = settings.PERMISSION_CLASSES


class MediaByCreator(ListAPIView):
    """
    Generic view to get media by creator id
    """

    serializer_class = MediaSerializer
    authentication_classes = settings.AUTHENTICATION_CLASSES
    permission_classes = settings.PERMISSION_CLASSES

    def get_queryset(self):
        """
        This should return the list of media by creator id
        """

        queryset = []
        creator_id = self.kwargs['creator']
        if creator_id is not None:
            queryset = Media.objects.filter(
                creator__id=creator_id,
            )
        
        return queryset


class HistoryList(ListCreateAPIView):
    """
    view to get history list and post new history
    """

    queryset = History.objects.all()
    serializer_class = HistorySerializer
    authentication_classes = settings.AUTHENTICATION_CLASSES
    permission_classes = settings.PERMISSION_CLASSES


class HistoryGeneric(RetrieveUpdateDestroyAPIView):
    """
    generic view to get, put, delete 'history'
    """

    queryset = History.objects.all()
    serializer_class = HistorySerializer
    authentication_classes = settings.AUTHENTICATION_CLASSES
    permission_classes = settings.PERMISSION_CLASSES


class MediaByGenre(ListAPIView):
    """
    view to get media list by username
    """

    serializer_class = MediaSerializer
    authentication_classes = settings.AUTHENTICATION_CLASSES
    permission_classes = settings.PERMISSION_CLASSES

    def get_queryset(self):
        """
        This should return the list of media for the username
        """

        genre = self.kwargs['genre']
        queryset = []

        if genre is not None:
            genre = int(genre)
            queryset = Media.objects.filter(genre=genre)

        return queryset


class HistoryByUsername(ListAPIView):
    """
    View to get history list by username
    """

    serializer_class = HistorySerializer
    authentication_classes = settings.AUTHENTICATION_CLASSES
    permission_classes = settings.PERMISSION_CLASSES

    def get_queryset(self):
        """
        This should return the list of history for the username
        """

        username = self.kwargs['username']
        queryset = []

        if username is not None:
            queryset = History.objects.filter(
                user__username=username,
            )

        return queryset


class HistoryByUserAndGenre(BaseListAPIView):
    """
    View to get history by username and genre
    """

    serializer_class = HistorySerializer

    def get_queryset(self):
        """
        This should return the history list by username and genre
        """

        username = self.kwargs['username']
        genre = self.kwargs['genre']

        queryset = []

        if username != username:
            return queryset
        
        if genre != genre:
            queryset = History.objects.filter(
                user__username=username,
            )
        else:
            queryset = History.objects.filter(
                user__username=username,
                media__genre=genre,
            )
        

        return queryset
