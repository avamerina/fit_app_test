from django.contrib.auth import get_user_model
from django.db import models


class Gym(models.Model):
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    admin = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - {self.address}"

    class Meta:
        db_table = 'gyms'
