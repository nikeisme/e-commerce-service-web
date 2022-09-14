from django.db import models
from commons.models import TimeStampedModel
from users.models import User

# Create your models here.

class Product(TimeStampedModel):

    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(default=0,max_digits = 13, decimal_places = 2)
    description = models.CharField(max_length=500)
    stock = models.IntegerField(default=1)

    class Meta:
        db_table = "products"

    def __str__(self):
        return self.name

