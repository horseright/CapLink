# Generated by Django 4.0.3 on 2022-04-05 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField(blank=True, null=True)),
                ('company', models.CharField(blank=True, max_length=255, null=True)),
                ('subject', models.CharField(blank=True, max_length=255, null=True)),
                ('message', models.TextField()),
            ],
        ),
    ]
