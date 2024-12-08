from django.contrib import admin
from .models import *


@admin.register(Task_board)
class TaskBoard(admin.ModelAdmin):
    list_display = ['project_name','desc_project']


@admin.register(Task_desc)
class TaskDesc(admin.ModelAdmin):
    list_display = ['task_name','responcile']
    
    
@admin.register(add_project)
class test(admin.ModelAdmin):
    list_display =['name']
