"""
Author: Masum Billal
Define routing for the app 'users'
"""

from django.urls import path

from users.views import (
    UserList,
)

urlpatterns = [
    path('list/', UserList.as_view(), name='user-list'),
]
