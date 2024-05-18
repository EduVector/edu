from rest_framework import serializers
from apps.structure.models import TaskSubmittion

class TaskSubmittionSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = TaskSubmittion
        fields = ['student', 'task', 'file', 'created_at', 'updated_at']
        extra_kwargs = {
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }
