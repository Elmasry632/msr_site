from django.urls import path
from . import views

urlpatterns = [
    path('', views.msr, name='task_boards'),
     path('board/<int:board_id>/', views.task_board, name='task_board'),
    path('tasks/', views.Task_desc, name='task_descriptions'),
    path('board/<int:board_id>/add/', views.add_project, name='add_project'),
    path('board/<int:board_id>/new_task/', views.add_task, name='add_task'),

]
