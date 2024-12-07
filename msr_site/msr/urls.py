from django.urls import path
from . import views

urlpatterns = [
    path('', views.msr, name='home'),
    path('msr/<int:board_id>/', views.board_topics, name="board_topics"),
    path('msr/task/',views.task_board, name="task_desc"),
    path('msr/<int:board_id>/new/', views.test_board, name="test_board"),
]
