# Generated by Django 3.1.2 on 2020-10-05 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_remove_profile_minutes_spent'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]