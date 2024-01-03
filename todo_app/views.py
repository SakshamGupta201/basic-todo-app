from django.http import HttpResponse
from django.shortcuts import redirect, render
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
                return redirect('home')
            else:
                return HttpResponse("Title cannot be empty")
        except Exception as e:
            print(e)
            return HttpResponse("Error occurred while processing the form")
