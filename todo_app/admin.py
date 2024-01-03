from django.contrib import admin

from todo_app.models import Todo

# Register your models here.


class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_completed', 'updated_at')
    search_fields = ('title',)


admin.site.register(Todo, TodoAdmin)
