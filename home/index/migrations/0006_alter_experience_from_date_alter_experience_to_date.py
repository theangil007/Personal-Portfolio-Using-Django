# Generated by Django 4.1.1 on 2024-01-01 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_alter_experience_from_date_alter_experience_to_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='from_date',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='experience',
            name='to_date',
            field=models.CharField(max_length=50),
        ),
    ]