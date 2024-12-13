from django.contrib import admin
from .models import *
@admin.register(Task_board)
class TaskBoardAdmin(admin.ModelAdmin):
    list_display = ['project_name', 'desc_project', 'created_by', 'created_on']
    search_fields = ['project_name', 'desc_project']
    list_filter = ['created_by', 'created_on']
    ordering = ['created_on']
@admin.register(Task_desc)
class TaskDescriptionAdmin(admin.ModelAdmin):
    list_display = ['task_name', 'responsible', 'board', 'created_by', 'created_on']
    search_fields = ['task_name', 'responsible', 'task_desc']
    list_filter = ['board', 'created_on', 'created_by']
    ordering = ['created_on']