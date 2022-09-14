from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from orders.models import Order
from orders.serializers import OrderCreateSerializer


class OrderView(viewsets.ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer
    permission_classes = [IsAuthenticated]

