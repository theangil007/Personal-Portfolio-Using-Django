# Generated by Django 4.1.1 on 2024-01-06 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0013_project_project_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='language3',
        ),
    ]