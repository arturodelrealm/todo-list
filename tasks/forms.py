from django import forms
from .models import Task


class TaskForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['due_date'].required = False
        self.fields['time_estimate'].required = False
        if not self.instance.pk:
            self.fields['time_estimate'].readonly = True

    class Meta:
        model = Task
        fields = ["title", "description", "due_date", "time_estimate"]

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "due_date": forms.DateInput(
                attrs={"class": "form-control"}
            ),
            "time_estimate": forms.TextInput(attrs={"class": "form-control"}),

        }
