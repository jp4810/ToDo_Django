"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apps.tasks import views

urlpatterns = [
    path('', views.TasksView.as_view(), name='tasks_view'),
    path('change_task/<int:task_id>', views.ChangeTaskState.save, name='change_task'),
    path('task_detail/<int:task_id>', views.TaskDetailView.as_view(), name='task_detail'),
    path('new_task/', views.AddTaskView.as_view(), name='new_task'),
]
