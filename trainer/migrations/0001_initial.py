# Generated by Django 5.0.4 on 2024-04-05 08:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gym', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('base_profile', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, related_name='trainer', serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='base_profile')),
                ('specialization', models.CharField(choices=[('personal_training', 'Personal Training'), ('functional_training', 'Functional Training'), ('strength_training', 'Strength Training'), ('cardio_training', 'Cardio Training'), ('beginner_fitness', 'Beginner Fitness'), ('functional_nutrition', 'Functional Nutrition'), ('group_training', 'Group Training'), ('flexibility_stretching', 'Flexibility & Stretching')], default='group_training', max_length=150)),
                ('gyms', models.ManyToManyField(related_name='trainers', to='gym.gym')),
            ],
        ),
    ]