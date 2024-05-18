from rest_framework import serializers
from apps.structure.models import Payment

class PaymentSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Payment
        fields = ['student', 'price', 'date', 'deadline', 'comment', 'created_at', 'updated_at']
        extra_kwargs = {
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }