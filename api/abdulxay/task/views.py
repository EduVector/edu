from rest_framework import generics
from .serializers import TaskSerializers
from apps.structure.models import Task

class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class =  TaskSerializers