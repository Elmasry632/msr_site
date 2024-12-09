from django import forms
from .models import *

class AddProjectForm(forms.Form):
    project_name = forms.CharField(max_length=30, label="Project Name")
    description = forms.CharField(
        widget=forms.Textarea, max_length=150, label="Project Description"
    )



class TaskDescForm(forms.ModelForm):
    class Meta:
        model = Task_desc
        fields = ['task_name', 'responsible', 'task_desc', 'board']
        labels = {
            'task_name': 'Task Name',
            'responsible': 'Responsible',
            'task_desc': 'Task Description',
            'board': 'Task Board'
        }
        widgets = {
            'task_desc': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter task description'}),
            'board': forms.Select(attrs={'class': 'form-control'})
        }