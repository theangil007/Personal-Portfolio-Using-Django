# Generated by Django 4.1.1 on 2024-01-07 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0014_remove_project_language3'),
    ]

    operations = [
        migrations.AddField(
            model_name='about_me',
            name='profile_pic_url',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]