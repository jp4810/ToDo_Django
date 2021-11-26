from django import forms

class TaskForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(max_length=500, required=False)

