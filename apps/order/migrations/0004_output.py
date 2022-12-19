# Generated by Django 4.0.3 on 2022-04-05 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_alter_order_order_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Output',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=255)),
                ('pool', models.CharField(max_length=255)),
                ('production', models.DecimalField(decimal_places=4, max_digits=9)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='production', to='order.order')),
            ],
        ),
    ]