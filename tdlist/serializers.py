from rest_framework import serializers
from .models import Task
from django.utils import timezone


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


        def validate_task_time(self, value):
            current_time = timezone.now().time()
            if value and value < current_time:
                raise serializers.ValidationError("Task can't be in the past.")
            if value.hour > 23 or (value.hour and value.minute > 59):
                raise serializers.ValidationError("Invalid task time.")
            return value

