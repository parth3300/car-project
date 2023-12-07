# Generated by Django 4.2.7 on 2023-11-29 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0031_car_carowned_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='carowner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='carowned', to='store.carowner'),
            preserve_default=False,
        ),
    ]