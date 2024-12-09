from django.db import models
from django.contrib.auth.models import User
class Task_board(models.Model):
    project_name = models.CharField(max_length=30, verbose_name="Project Name")
    desc_project = models.CharField(max_length=150, verbose_name="Project Description")
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name="created_boards",verbose_name="Created By",)
    created_on = models.DateTimeField(auto_now_add=True, verbose_name="Created On")
    def __str__(self):
        return self.project_name
    class Meta:
        verbose_name = "Task Board"
        verbose_name_plural = "Task Boards"
        ordering = ["-created_on"]
class Task_desc(models.Model):
    task_name = models.CharField(max_length=20, verbose_name="Task Name")
    responsible = models.CharField(max_length=30, verbose_name="Responsible")
    task_desc = models.CharField(max_length=150, verbose_name="Task Description")
    board = models.ForeignKey(Task_board,on_delete=models.CASCADE,
        related_name="tasks",
        null=True,
        blank=True,
        verbose_name="Task Board",
    )
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name="created_tasks",verbose_name="Created By",)
    created_on = models.DateTimeField(auto_now_add=True, verbose_name="Created On")
    def __str__(self):
        return self.task_name
    class Meta:
        verbose_name = "Task Description"
        verbose_name_plural = "Task Descriptions"
        ordering = ["-created_on"]
class add_project(models.Model):
    name = models.CharField(max_length=20, verbose_name="Project Name")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Add Project"
        verbose_name_plural = "Add Projects"