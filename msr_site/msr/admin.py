from django.contrib import admin
from .models import Task_board
from .models import Task_desc
@admin.register(Task_board)
class TaskBoard(admin.ModelAdmin):
    list_display = ['project_name','desc_project']

# @admin.register(Task_desc)
class TaskDesc(admin.ModelAdmin):
    list_display = ['task_name','desc_task']
