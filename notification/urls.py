from rest_framework import routers

from notification import views

router = routers.DefaultRouter()
router.register('notifications', views.NotificationViewSet)

urlpatterns = router.urls
