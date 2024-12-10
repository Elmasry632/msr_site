from django import forms
from .models import *

class AddProjectForm(forms.Form):
    project_name = forms.CharField(max_length=30, label="Project Name")
    description = forms.CharField(widget=forms.Textarea, max_length=150, label="Project Description")
    # ---------------------------------task -------------------------------
    task_name= forms.CharField(max_length=30, label="Task Name")
    responsible=forms.CharField(max_length=30, label="Responsiple")
    task_desc=forms.CharField(widget=forms.Textarea, max_length=150, label="Task Description")
    board=project_name