from django.urls import path
from . import views

urlpatterns = [
    path('', views.msr, name='msr'),
    path('msr/<int:board_id>/', views.board_topics, name="board_topics")
]
