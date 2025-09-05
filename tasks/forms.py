from django import forms
from .models import Task


class TaskForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['due_date'].required = False

    class Meta:
        model = Task
        fields = ["title", "description", "due_date"]

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.TextInput(attrs={"class": "form-control"}),
            "due_date": forms.DateInput(
                attrs={"class": "form-control"}
            ),
        }
