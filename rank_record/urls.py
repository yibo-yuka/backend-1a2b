from django.urls import path
from .views import UserScoreListCreateView

urlpatterns = [
    path('scores/', UserScoreListCreateView.as_view(), name='score-list-create'),
]