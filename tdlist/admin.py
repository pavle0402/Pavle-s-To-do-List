from django.contrib import admin
from .models import Task, TaskCompletion, Contact


admin.site.register(Task)
admin.site.register(TaskCompletion)
admin.site.register(Contact)