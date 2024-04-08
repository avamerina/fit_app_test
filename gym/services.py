from gym.models import Gym


def get_gym_by_id(pk):
    return Gym.objects.get(pk=pk)
