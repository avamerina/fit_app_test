from rest_framework.routers import DefaultRouter

from trainer.views import TrainerViewSet

router = DefaultRouter()
router.register(r'trainers', TrainerViewSet, basename='trainers')

urlpatterns = router.urls
