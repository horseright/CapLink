# Generated by Django 4.0.3 on 2022-03-19 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_faq_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='estimated_starting_hours',
            field=models.IntegerField(default=72),
        ),
    ]
