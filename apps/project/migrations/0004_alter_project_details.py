# Generated by Django 4.0.3 on 2022-03-27 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_project_estimated_starting_hours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='details',
            field=models.ImageField(upload_to='details'),
        ),
    ]
