from django.urls import path
from todo_app import views


urlpatterns = [
    path("addTask", views.TaskView.as_view(), name="addTask"),
    path('update/<int:pk>', views.update, name="update"),
    path('mark_done/<int:pk>', views.mark_done, name="mark_done"),
    path('mark_undone/<int:pk>', views.mark_undone, name="mark_undone"),
    path('delete/<int:pk>', views.mark_done, name="delete"),
]
