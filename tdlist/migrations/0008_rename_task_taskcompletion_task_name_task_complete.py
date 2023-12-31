# Generated by Django 4.2.3 on 2023-08-14 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tdlist', '0007_task_pinned'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taskcompletion',
            old_name='task',
            new_name='task_name',
        ),
        migrations.AddField(
            model_name='task',
            name='complete',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tdlist.taskcompletion'),
        ),
    ]
