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
    week_day = models.IntegerField(choices=DAY_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f'{self.trainer.base_profile.get_full_name()} {self.gym.title}'

    class Meta:
        unique_together = ('trainer', 'gym', 'week_day', 'start_time', 'end_time')
