from django.db.models import query
from django.views.generic import ListView
from django.shortcuts import redirect
from apps.tasks.models import Tasks

class TasksView(ListView):
    model = Tasks
    template_name = "tasks_view.html"

    def get_context_data(self):
        tasks_list = Tasks.objects.raw(
                """
                SELECT id, state, title, created_at
                FROM tasks
                ORDER BY state ASC, created_at DESC
                """
            )
        context={
            'tasks_list': tasks_list
        }
        return context
    
class ChangeTaskState():
    def save(request, **kwargs):
        if 'task_id' in kwargs.keys():
            try:
                mod_task = Tasks.objects.filter(id=kwargs['task_id']).first()
                mod_task.state = not mod_task.state
                mod_task.save()
            except:
                pass
        return redirect('tasks_view')
