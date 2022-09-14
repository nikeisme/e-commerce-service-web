from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from payments.models import Payment
from payments.serializers import PaymentSerializer




class PaymentView(viewsets.ModelViewSet):

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

