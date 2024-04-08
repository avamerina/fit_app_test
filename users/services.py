from users.models import BaseProfile


def get_base_profile_by_id(pk):
    return BaseProfile.objects.get(pk=pk)
