# Generated by Django 4.1.1 on 2024-01-06 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0009_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='certifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=50)),
                ('institute', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Certifications',
                'verbose_name_plural': 'Certifications',
            },
        ),
    ]
