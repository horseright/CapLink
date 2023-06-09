# Generated by Django 4.0.3 on 2022-03-31 13:28

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.UUIDField(default=uuid.uuid4)),
                ('service_product', models.CharField(max_length=255)),
                ('pool', models.CharField(max_length=255)),
                ('start_time', models.DateTimeField()),
                ('longth', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('output', models.DecimalField(decimal_places=4, max_digits=9)),
                ('status', models.CharField(choices=[('normal', 'normal'), ('repair', 'repair'), ('waiting', 'waiting')], max_length=10)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'orders',
            },
        ),
    ]
