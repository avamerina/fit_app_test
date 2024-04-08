from notification.models import Notification


def notification_create(data):
    notification = Notification.objects.create(**data)
    notification.save()
    return notification
