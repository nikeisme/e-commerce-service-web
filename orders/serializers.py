from django.db import transaction
from rest_framework import serializers

from orders.models import Order


class OrderCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = "__all__"
        




