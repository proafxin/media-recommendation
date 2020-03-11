from django.urls import path, include
from .views import SingerListView, SingerDetailView

urlpatterns = [
    path('singers/', SingerListView.as_view(), name='singers'),
    path('singer/<int:pk>/', SingerDetailView.as_view(), name='singer'),
]