from django.http import HttpResponse
from django.shortcuts import render
from todo_app.models import Todo


def home(request):
    tasks = Todo.objects.filter(is_completed=False).order_by('-updated_at')
    completed_tasks = Todo.objects.filter(is_completed=True).order_by('-updated_at')
    return render(request, "home.html", {"tasks": tasks,'completed_tasks': completed_tasks})


