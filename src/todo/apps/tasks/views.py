from django.http import HttpResponse
from django.views.generic import ListView
from apps.tasks.models import Tasks
from apps.tasks.forms import TasksForm

class TasksView(ListView):
    model = Tasks
    template_name = "tasks_view.html"