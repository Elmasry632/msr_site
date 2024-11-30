from django.contrib import admin
from .models import Task_board
from .models import Task_desc

@admin.register(Task_board)
class TaskBoard(admin.ModelAdmin):
    list_display = ['project_name','desc_project']

admin.site.register(Task_desc)
class TaskDesc(admin.ModelAdmin):
    list_display = ['task_name','task_desc','responcile']
    

