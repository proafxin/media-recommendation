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
    MediaList,
    MediaGeneric,
    MediaByCreator,
    MediaByGenre,
    HistoryList,
    HistoryGeneric,
    HistoryByUsername,
    HistoryByUserAndGenre,
)

urlpatterns = [
    path('creators/', CreatorList.as_view(), name='creators'),
    path('creator/<int:pk>/', CreatorGeneric.as_view(), name='creator'),
    path('media/<int:pk>/', MediaGeneric.as_view(), name='media'),
    path('medias/', MediaList.as_view(), name='medias'),
    path('histories/', HistoryList.as_view(), name='histories'),
    path('histories/<int:pk>/', HistoryGeneric.as_view(), name='history'),
    path('medias/genre/<int:genre>/', MediaByGenre.as_view()),
    path('histories/username/<str:username>/', HistoryByUsername.as_view()),
    path('medias/creator/<int:creator>/', MediaByCreator.as_view()),
    path('histories/username/<str:username>/genre/<int:genre>', HistoryByUserAndGenre.as_view()),
]
