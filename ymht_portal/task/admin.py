from django.contrib import admin
from .models import Task, TaskCategory

admin.site.register(TaskCategory)
admin.site.register(Task)
