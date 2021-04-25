"""
Author: Masum Billal
Define serializers for 'users' app
"""

from django.contrib.auth.models import User

from rest_framework.serializers import ModelSerializer

class UserSerializer(ModelSerializer):
    """
    Serializer for default user model
    """

    class Meta:
        """
        Specify which model and fields to use
        """

        model = User
        fields = '__all__'
