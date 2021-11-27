from django.db.models import query
from django.views.generic import ListView, FormView
from django.shortcuts import redirect
from apps.tasks.models import Tasks
from apps.tasks.forms import TaskForm

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
    
class TaskDetailView(ListView):
    model = Tasks
    template_name = "task_detail_view.html"

    def get_context_data(self):
        task_id = self.request.get_full_path().split('/')[-1]
        task_details = Tasks.objects.filter(id=task_id).first()
        context={
            'task_details': task_details
        }
        return context

class AddTaskView(FormView):
    model=Tasks
    form = TaskForm
    template_name = "add_task_view.html"

    def get_context_data(self):
        last_task_id = Tasks.objects.raw(
            """
            SELECT id
            FROM tasks
            ORDER BY id DESC
            LIMIT 1
            """
        )[0].id
        context={
            'new_id': last_task_id+1,
            'form': self.form
        }
        return context
    
    def post(self, request):
        Tasks.objects.get_or_create(title=request.POST.dict()['title'], description=request.POST.dict()['description'])
        return redirect('tasks_view')

class ChangeTask():
    def save(request, **kwargs):
        if 'task_id' in kwargs.keys():
            try:
                mod_task = Tasks.objects.filter(id=kwargs['task_id']).first()
                mod_task.state = not mod_task.state
                mod_task.save()
            except:
                pass
        return redirect('tasks_view')
    def delete(request, **kwargs):
        if 'task_id' in kwargs.keys():
            try:
                mod_task = Tasks.objects.filter(id=kwargs['task_id']).first()
                mod_task.delete()
            except:
                pass
        return redirect('tasks_view')
