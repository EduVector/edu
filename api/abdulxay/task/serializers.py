from rest_framework import serializers
from apps.structure.models import Task

class TaskSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        fields = ['title', 'grade', 'deadline', 'created_at', 'updated_at', 'teacher', 'group', 'file']
        
        extra_kwargs = {
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }
