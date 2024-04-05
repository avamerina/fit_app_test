from django.db import models

from gym.models import Gym
from trainer.models import Trainer


class ScheduleUnit(models.Model):
    DAY_CHOICES = [
        (0, 'Monday'),
        (1, 'Tuesday'),
        (2, 'Wednesday'),
        (3, 'Thursday'),
        (4, 'Friday'),
        (5, 'Saturday'),
        (6, 'Sunday')
    ]
    trainer = models.ForeignKey(Trainer, on_delete=models.DO_NOTHING)
    gym = models.ForeignKey(Gym, on_delete=models.DO_NOTHING)
    week_day = models.IntegerField(choices=DAY_CHOICES, default=0)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f'{self.trainer.base_profile.name} {self.gym.title}'
