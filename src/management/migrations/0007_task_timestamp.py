# Generated by Django 3.1.2 on 2020-10-05 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0006_task_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
