from django import forms
 
class TasksForm(forms.Form):
    title = forms.CharField()
