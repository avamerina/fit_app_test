from django.contrib.auth import get_user_model
from django.db import models


class Notification(models.Model):
    NOTIFICATION_TYPES = [
        ('appointment', 'Appointment'),
        ('client', 'Client')
    ]

    receiver = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='notifications')
    notification_type = models.CharField(max_length=50, choices=NOTIFICATION_TYPES)
    description = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'notifications'
