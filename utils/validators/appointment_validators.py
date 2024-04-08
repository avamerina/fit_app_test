from django.utils import timezone

from django.db.models import Q

from schedule.services import get_all_schedule_units_by_trainer
from appointment.services import get_appointments_by_client, get_appointments_by_trainer_on_given_date


def date_validator_by_schedule_days(attrs):
    trainer = attrs['trainer']
    appointment_date = attrs['date']
    schedules = get_all_schedule_units_by_trainer(trainer).filter(week_day=appointment_date.weekday())
    if len(schedules) == 0:
        return True
    return False


def trainer_schedule_conflict_validator(attrs):
    trainer = attrs['trainer']
    appointment_date = attrs['date']
    gym = attrs['gym']
    schedule_units = get_all_schedule_units_by_trainer(trainer).filter(week_day=appointment_date.weekday(), gym=gym)
    units_with_no_conflict_to_appointment_time = schedule_units.filter(
        Q(start_time__lte=attrs['start_time']) &
        Q(start_time__lt=attrs['end_time']) &
        Q(end_time__gte=attrs['end_time']) &
        Q(end_time__gt=attrs['start_time'])
    )
    if len(units_with_no_conflict_to_appointment_time) > 0:
        return False
    return True


def client_appointment_conflicts_validator(attrs):
    client = attrs['client']
    appointment_date = attrs['date']
    appointments = get_appointments_by_client(client).filter(date=appointment_date)

    conflicting_appointments = appointments.filter(
        Q(start_time__lte=attrs['start_time']) & Q(end_time__gt=attrs['start_time']) |
        Q(end_time__gte=attrs['end_time']) & Q(start_time__lt=attrs['end_time']) |
        Q(start_time__lte=attrs['start_time']) & Q(end_time__gt=attrs['start_time'])
    )

    if len(conflicting_appointments) > 0:
        return True
    return False


def future_date_validator(attrs):
    date = attrs['date']
    if date < timezone.now().date():
        return True
    return False


def user_role_validator(attrs):
    client_role = attrs['client'].role
    trainer_role = attrs['trainer'].base_profile.role
    return client_role == 'client' and trainer_role == 'trainer'


def trainer_availability_validator(attrs):
    trainer = attrs.get('trainer')
    date = attrs.get('date')
    start_time = attrs.get('start_time')
    end_time = attrs.get('end_time')

    trainer_existing_appointments = get_appointments_by_trainer_on_given_date(trainer, date)

    appointments_conflicts = trainer_existing_appointments.filter(
        Q(start_time__gte=start_time) & Q(start_time__lt=end_time) |
        Q(end_time__gt=start_time) & Q(start_time__lte=start_time) |
        Q(start_time__exact=start_time) & Q(end_time__exact=end_time)
    )

    if len(appointments_conflicts) > 0:
        return True
    return False
