from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response

from .serializers import LineOfActionSerializer, DoctorSerializer
from info_doctor.models import LineOfAction, Doctor


class LineOfActionSerializerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows lines of actions to be viewed or edited.
    """
    queryset = LineOfAction.objects.all()
    serializer_class = LineOfActionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class DoctorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows doctors to be viewed or edited.
    """
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
