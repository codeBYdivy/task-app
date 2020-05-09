from django.urls import include, path
from rest_framework import routers

from .views import AssignmentViewSet, DemandViewSet

router = routers.DefaultRouter()
router.register('demands', DemandViewSet)
router.register('assignments', AssignmentViewSet)

urlpatterns = [
    path('', include(router.urls))
]
