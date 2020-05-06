from django.urls import path, include
from rest_framework import routers
from .views import DemandViewSet, AssignmentViewSet

router = routers.DefaultRouter()
router.register('demands', DemandViewSet)
router.register('assignments', AssignmentViewSet)

urlpatterns = [
    path('', include(router.urls))
]
