from rest_framework import routers

from appointment import views

router = routers.DefaultRouter()
router.register(r'appointments', views.AppointmentViewSet)

urlpatterns = router.urls
