from appointment.models import Appointment


def get_appointments_by_client(client):
    return Appointment.objects.filter(client=client)


def get_appointments_by_trainer_on_given_date(trainer, date):
    return Appointment.objects.filter(trainer=trainer).filter(date=date)
