from django import forms
from .models import TaskModel

class TaskForm(forms.ModelForm):
    class Meta:
        model=TaskModel
        fields="__all__"
        labels={
            "taskTitle":"Task Title",
            "taskDescription":"Description",
            "taskDate":"Date",
            "is_completed":"Complete"
        }
        widgets={
            "taskDate":forms.DateInput(attrs={"type":"date"})
        }