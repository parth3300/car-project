# Generated by Django 4.2.7 on 2023-11-29 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0032_car_carowner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='carowned_id',
        ),
    ]