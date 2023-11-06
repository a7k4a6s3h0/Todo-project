from django import forms
from . models import *

class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = User_Tasks
        fields = ['task_name', 'created_at', 'task_describtion']


class UpdateTaskForm(forms.ModelForm):
    class Meta:
        model = User_Tasks
        fields = ['task_name', 'task_describtion']
