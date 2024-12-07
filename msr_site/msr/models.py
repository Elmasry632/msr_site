from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Task_board(models.Model):
    project_name = models.CharField(max_length=30)
    desc_project = models.CharField(max_length=150)
    
class Task_desc(models.Model):
    task_name = models.CharField(max_length=20)
    responcile = models.CharField(max_length=30)
    task_desc = models.CharField(max_length=150)
    board = models.ForeignKey('Task_board', on_delete=models.CASCADE, default=None, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default='elmasry')  # Replace `1` with a valid user ID
    created_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task_name

class test(models.Model):
    name = models.CharField(max_length=20)