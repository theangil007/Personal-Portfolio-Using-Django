# Generated by Django 4.1.1 on 2024-01-02 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_alter_experience_from_date_alter_experience_to_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=50)),
                ('collage', models.CharField(max_length=50)),
                ('from_date', models.CharField(max_length=50)),
                ('to_date', models.CharField(max_length=50)),
                ('grade', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'Education',
                'verbose_name_plural': 'Education',
            },
        ),
    ]
