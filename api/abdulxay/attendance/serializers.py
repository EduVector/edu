from rest_framework import serializers
from apps.structure.models import Attendance

class AttendanceSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Attendance
        fields = ['lesson', 'student', 'status', 'created_at', 'updated_at']
        extra_kwargs = {
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }
        
