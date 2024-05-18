from rest_framework import generics
from .serializers import PaymentSerializers
from apps.structure.models import Payment


class PaymentListView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class =  PaymentSerializers