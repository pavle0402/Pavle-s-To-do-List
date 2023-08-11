from rest_framework import serializers
from .models import Task
from django.utils import timezone


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


        def validate_task_time(self, value):
            if value and value < timezone.now().time():
                raise serializers.ValidationError("Task can't be in the past.")
            return value

