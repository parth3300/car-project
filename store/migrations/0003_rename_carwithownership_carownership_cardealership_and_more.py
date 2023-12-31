# Generated by Django 5.0 on 2023-12-23 08:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_carwithdealership_dealerships_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CarWithOwnerShip',
            new_name='CarOwnerShip',
        ),
        migrations.CreateModel(
            name='CarDealerShip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='dealership', to='store.car')),
                ('dealership', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars_at_dealership', to='store.dealership')),
            ],
        ),
        migrations.DeleteModel(
            name='CarWithDealerShip',
        ),
    ]
