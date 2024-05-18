from rest_framework import generics
from .serializers import AttendanceSerializers
from apps.structure.models import Attendance

class AttendanceListView(generics.ListAPIView):
    queryset = Attendance.objects.all()
    serializer_class =  AttendanceSerializers