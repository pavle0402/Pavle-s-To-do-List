from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    task = models.TextField(verbose_name="Task")
    task_due = models.TimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    pinned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.task} - {self.user}"
    
    class Meta:
        ordering = ['task_due']
    

class TaskCompletion(models.Model):
    task = models.OneToOneField(Task, on_delete=models.CASCADE, related_name='completion')
    task_completion = models.BooleanField(default=False)