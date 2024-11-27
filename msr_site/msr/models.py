from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Task_board(models.Model):
    project_name = models.CharField(max_length=30)
    desc_project = models.CharField(max_length=150)

class Task_desc(models.Model):
    task_name = models.CharField(max_length=20)
    responcile = models.CharField(max_length=30)
    board=models.ForeignKey(Task_board,related_name='Tasks',on_delete=models.CASCADE)
    created_by=models.ForeignKey(User,related_name='TAsks',on_delete=models.CASCADE)
    created_on=models.DateTimeField(auto_now_add=True)


    
    def __str__(self):
        return self.title