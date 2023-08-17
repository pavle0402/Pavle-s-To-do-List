from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError

class TaskOrderManager(models.Manager):

    def pinned_first(self):
        return self.get_queryset().order_by('-pinned', 'task')
    
    def alphabetical(self):
        return self.get_queryset().order_by('task')

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    task = models.TextField(verbose_name="Task")
    task_due = models.TimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    pinned = models.BooleanField(default=False)
    complete = models.ForeignKey("TaskCompletion", on_delete=models.CASCADE, null=True)
    objects = TaskOrderManager()

    def __str__(self):
        return f"{self.task} - {self.user}"
    

class TaskCompletion(models.Model):
    task_name = models.OneToOneField(Task, on_delete=models.CASCADE, related_name='completion')
    task_completion = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.task_name.task}"