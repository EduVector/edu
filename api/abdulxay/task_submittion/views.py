from rest_framework import generics
from .serializers import TaskSubmittionSerializers
from apps.structure.models import TaskSubmittion

class TaskSubmittionListView(generics.ListAPIView):
    queryset = TaskSubmittion.objects.all()
    serializer_class =  TaskSubmittionSerializers