# Generated by Django 4.2.16 on 2024-11-23 21:00

import django.contrib.postgres.indexes
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationdata',
            name='device_id',
            field=models.CharField(db_index=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='locationdata',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
        migrations.AlterIndexTogether(
            name='locationdata',
            index_together={('device_id', 'timestamp', 'latitude', 'longitude')},
        ),
        migrations.AddIndex(
            model_name='locationdata',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['timestamp'], name='locations_l_timesta_79c033_brin'),
        ),
    ]