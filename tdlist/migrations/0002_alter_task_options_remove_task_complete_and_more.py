# Generated by Django 4.2.3 on 2023-08-04 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tdlist', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={},
        ),
        migrations.RemoveField(
            model_name='task',
            name='complete',
        ),
        migrations.CreateModel(
            name='TaskCompletion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_completion', models.BooleanField(default=False)),
                ('task', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='completion', to='tdlist.task')),
            ],
        ),
    ]
