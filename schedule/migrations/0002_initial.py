# Generated by Django 5.0.4 on 2024-04-05 08:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('schedule', '0001_initial'),
        ('trainer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='scheduleunit',
            name='trainer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='trainer.trainer'),
        ),
    ]
