from django.urls import include, path
from rest_framework import routers

from .views import EmployeeViewSet, UserViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('employees', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls))
]
