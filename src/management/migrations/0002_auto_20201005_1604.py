# Generated by Django 3.1.2 on 2020-10-05 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='minutes_spent',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]