from django.http import QueryDict
from schedule.models import ScheduleUnit


def get_all_schedule_units_by_trainer(trainer):
    return ScheduleUnit.objects.filter(trainer=trainer)


def get_schedule_units_by_gym(gym):
    return ScheduleUnit.objects.filter(gym=gym)


def get_schedule_units_by_trainer_specification(specialization) -> QueryDict:
    return ScheduleUnit.objects.filter(trainer__specialization=specialization)
