from django.contrib.auth import get_user_model
from django.db import models

from gym.models import Gym


class Trainer(models.Model):
    SPEC_CHOICES = [
        ('personal_training', 'Personal Training'),
        ('functional_training', 'Functional Training'),
        ('strength_training', 'Strength Training'),
        ('cardio_training', 'Cardio Training'),
        ('beginner_fitness', 'Beginner Fitness'),
        ('functional_nutrition', 'Functional Nutrition'),
        ('group_training', 'Group Training'),
        ('flexibility_stretching', 'Flexibility & Stretching'),
    ]
    base_profile = models.OneToOneField(
        to=get_user_model(),
        on_delete=models.DO_NOTHING,
        primary_key=True,
        related_name='trainer',
        verbose_name='base_profile'
    )
    specialization = models.CharField(max_length=150, choices=SPEC_CHOICES, default='group_training')
    gyms = models.ManyToManyField(Gym, related_name='trainers')

    def __str__(self):
        return f"{self.base_profile} - {self.specialization}"
