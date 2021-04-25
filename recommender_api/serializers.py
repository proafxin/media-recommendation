"""
Author: Masum Billal
Write serializers for 'media', 'creator' and 'history' models
"""

from rest_framework.serializers import ModelSerializer

from recommender_api.models import (
    Creator,
    Media,
    History,
)


class CreatorSerializer(ModelSerializer):
    """
    Serializer for the entity 'creator'
    """

    class Meta:
        """
        Specify fields for exposing 'creator' in JSON
        """

        model = Creator
        fields = '__all__'


class MediaSerializer(ModelSerializer):
    """
    Serializer for the entity 'media'
    """

    class Meta:
        """
        Specify fields for exposing 'media' in JSON
        """

        model = Media
        fields = '__all__'


class HistorySerializer(ModelSerializer):
    """
    Serializer for the entity 'history'
    """

    class Meta:
        """
        Specify fields for exposing 'history' in JSON
        """

        model = History
        fields = '__all__'
