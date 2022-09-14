from django.contrib.auth import get_user_model
from django.db import models

from commons.models import TimeStampedModel


class Order(TimeStampedModel):

    # 문자열이 들어가지 않고 클래스가 들어가야 하므로 get_user_model 적용
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=False, blank=False)
    address = models.CharField(max_length=300)
    recipient = models.CharField(max_length=20)

    class Meta:
        db_table = "orders"