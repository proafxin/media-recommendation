"""
Author: Masum Billal
routes for /api/recommender/
"""

from django.urls import (
    path,
)

from recommender_api.views import (
    CreatorList,
    CreatorGeneric,
)

urlpatterns = [
    path('creators/', CreatorList.as_view(), name='creators'),
    path('creator/<int:pk>/', CreatorGeneric.as_view(), name='creator'),
]
