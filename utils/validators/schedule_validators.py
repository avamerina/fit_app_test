from django.db.models import Q
from schedule.models import ScheduleUnit


def conflicting_trainer_schedule_units(attrs: dict) -> bool:
    conflicting_units_by_trainer = ScheduleUnit.objects.filter(
        Q(trainer__exact=attrs["trainer"]),
        Q(week_day__exact=attrs["week_day"]),
        (
                Q(start_time__lte=attrs['start_time']) & Q(end_time__gt=attrs['start_time']) |
                Q(start_time__lt=attrs['end_time']) & Q(end_time__gte=attrs['end_time'])
        ) |
        (
                Q(start_time__gt=attrs['end_time']) & Q(start_time__gte=attrs['start_time'])
        ) |
        (
                Q(end_time__gt=attrs['start_time']) & Q(end_time__lte=attrs['end_time'])
        ) |
        (
                Q(end_time__gte=attrs['end_time']) & Q(start_time__gte=attrs['start_time'])
        )
    )

    if len(conflicting_units_by_trainer) > 0:
        return True
    return False


def conflicting_gym_schedule_units(attrs: dict) -> bool:
    conflicting_units_by_gym = ScheduleUnit.objects.filter(
        Q(gym__exact=attrs["gym"]),
        Q(week_day__exact=attrs["week_day"]),
        (
                Q(start_time__lte=attrs['start_time']) & Q(end_time__gt=attrs['start_time']) |
                Q(start_time__lt=attrs['end_time']) & Q(end_time__gte=attrs['end_time'])
        ) |
        (
                Q(start_time__gt=attrs['end_time']) & Q(start_time__gte=attrs['start_time'])
        ) |
        (
                Q(end_time__gt=attrs['start_time']) & Q(end_time__lte=attrs['end_time'])
        ) |
        (
                Q(end_time__gte=attrs['end_time']) & Q(start_time__gte=attrs['start_time'])
        )
    )

    if len(conflicting_units_by_gym) > 0:
        return True
    return False
