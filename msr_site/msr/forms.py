from django import forms

class AddProjectForm(forms.Form):
    project_name = forms.CharField(max_length=30, label="Project Name")
    description = forms.CharField(
        widget=forms.Textarea, max_length=150, label="Project Description"
    )
