from django.test import TestCase
from apps.tasks import views
from django.urls import reverse
from apps.tasks.models import Tasks
from random import randint


class TestTasksModel(TestCase):
    number_of_tasks = 5
    def setUp(self):
        for task_id in range(1, self.number_of_tasks):
            Tasks.objects.create(id=task_id, title=f"Title {task_id}", description=f"Description {task_id}")

    def test_has_title(self):
        rand_id = randint(1, self.number_of_tasks-1)
        task = Tasks.objects.get(id=rand_id)
        self.assertEqual(task.title, f'Title {rand_id}')
    
    def test_has_description(self):
        rand_id = randint(1, self.number_of_tasks-1)
        task = Tasks.objects.get(id=rand_id)
        self.assertEqual(task.description, f'Description {rand_id}')
    
    def test_has_state_false(self):
        rand_id = randint(1, self.number_of_tasks-1)
        task = Tasks.objects.get(id=rand_id)
        self.assertEqual(task.state, False)

    def test_tasks_view_exists(self):
        response = self.client.get(reverse('tasks_view'))
        self.assertEqual(response.status_code, 200)

    
