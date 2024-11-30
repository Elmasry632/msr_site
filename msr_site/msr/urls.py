from django.urls import path
from . import views

urlpatterns = [
    path('', views.msr),
    path('msr/<int:board_id>/', views.board_topics,name="topics")
]
