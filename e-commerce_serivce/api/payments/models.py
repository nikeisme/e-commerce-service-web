from django.db import models
from commons.models import TimeStampedModel
from orders.models import Order

class Payment(TimeStampedModel):

    PAYMENT_STATUS = [
        ("결제완료", 'Payment completed',),
        ("결제대기", 'waiting for payment'),
    ]

    PAYMENT_METHODS = [
        ("신용카드","Credit card"),
        ("무통장입금","Deposit without bankbook"),
    ]

    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False, blank=False)
    payment_status = models.CharField(max_length=4, choices=PAYMENT_STATUS, null=True, blank=True)
    payment_method = models.CharField(max_length=5, choices=PAYMENT_METHODS,null=True, blank=True)

    class Meta:
        db_table = "payments"