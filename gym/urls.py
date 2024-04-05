from rest_framework import routers

from gym.views import GymViewSet

router = routers.DefaultRouter()
router.register(r'gyms', GymViewSet, basename='gyms')

urlpatterns = router.urls