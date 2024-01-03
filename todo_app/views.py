from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from todo_app.models import Todo

# Create your views here.


class TaskView(View):
    def post(self, request):
        try:
            task = request.POST.get("task")

            # Check if title is present and not empty
            if task:
                print(task)
                Todo.objects.create(title=task)
                return redirect("home")
            else:
                return HttpResponse("Title cannot be empty")
        except Exception as e:
            print(e)
            return HttpResponse("Error occurred while processing the form")


def mark_done(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.is_completed = True
    todo.save()
    return redirect("home")


def mark_undone(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.is_completed = False
    todo.save()
    return redirect("home")


def delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return redirect("home")


def update(request, pk):
    if request.method == "GET":
        todo = get_object_or_404(Todo, pk=pk)
        return render(request, "edit_todo.html", {"todo": todo})
    else:
        todo = get_object_or_404(Todo, pk=pk)
        title = request.POST.get("task")
        todo.title = title
        todo.save()
        return redirect("home")