"""
Author: Masum Billal
routes for /api/recommender/
"""

from django.urls import (
    path,
    re_path,
)

from recommender_api.views import (
    CreatorList,
    CreatorGeneric,
    MediaList,
    MediaGeneric,
    MediaByGenre,
    HistoryList,
    HistoryGeneric,
    HistoryByUsername,
)

urlpatterns = [
    path('creators/', CreatorList.as_view(), name='creators'),
    path('creator/<int:pk>/', CreatorGeneric.as_view(), name='creator'),
    path('media/<int:pk>/', MediaGeneric.as_view(), name='media'),
    path('medias/', MediaList.as_view(), name='medias'),
    path('histories/', HistoryList.as_view(), name='histories'),
    path('histories/<int:pk>/', HistoryGeneric.as_view(), name='history'),
    path('medias/genre/<int:genre>/', MediaByGenre.as_view(), name='media-by-genre'),
    path('histories/username/<str:username>/', HistoryByUsername.as_view(), name='history-by-username'),
]
