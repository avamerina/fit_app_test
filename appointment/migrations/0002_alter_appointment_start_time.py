# Generated by Django 5.0.4 on 2024-04-07 10:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='start_time',
            field=models.TimeField(default=datetime.time(10, 32, 55, 58461)),
        ),
    ]