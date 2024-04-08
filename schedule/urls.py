from rest_framework import routers
from schedule.views import ScheduleUnitViewSet


router = routers.DefaultRouter()
router.register(r'schedule_units', ScheduleUnitViewSet, basename='schedule_units')

urlpatterns = router.urls
