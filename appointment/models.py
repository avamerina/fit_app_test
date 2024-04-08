from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

from gym.models import Gym
from trainer.models import Trainer


class Appointment(models.Model):
    client = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING)
    trainer = models.ForeignKey(Trainer, on_delete=models.DO_NOTHING)
    gym = models.ForeignKey(Gym, on_delete=models.DO_NOTHING)
    date = models.DateField(default=timezone.now().date())
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.trainer} {self.date} {self.client}"

    class Meta:
        unique_together = (
            ('client', 'trainer', 'gym', 'date', 'start_time', 'end_time'),
            ('client', 'gym', 'date', 'start_time', 'end_time'),
            ('trainer', 'gym', 'date', 'start_time', 'end_time'),
        )
        db_table = 'appointments'
