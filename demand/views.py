from .models import Demand, Assignment
from .serializers import DemandSerializer, AssignmentSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication


class DemandViewSet(viewsets.ModelViewSet):
    serializer_class = DemandSerializer
    queryset = Demand.objects.all()
    authentication_classes = (TokenAuthentication, )


class AssignmentViewSet(viewsets.ModelViewSet):
    serializer_class = AssignmentSerializer
    queryset = Assignment.objects.all()
    authentication_classes = (TokenAuthentication, )
