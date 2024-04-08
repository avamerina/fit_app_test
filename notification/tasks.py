from core.celery import app
from notification.services import notification_create
from users.services import get_base_profile_by_id
from gym.services import get_gym_by_id


@app.task(ignore_results=False)
def create_trainer_notification(data):
    client = get_base_profile_by_id(data['client'])
    gym = get_gym_by_id(data['gym'])
    data = {
        'receiver': get_base_profile_by_id(data['trainer']),
        'notification_type': 'appointment',
        'description': f"New appointment on {data['date']}. Time: {data['start_time']}-{data['end_time']}, "
                       f"with {client.get_full_name()} at {gym.title}"

    }
    notification_create(data)
