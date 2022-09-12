from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from commons.models import TimeStampedModel


class User(AbstractUser,TimeStampedModel,models.Model):

    GENDERS = (
        ('M', '남성(Man)'),
        ('W', '여성(Woman)'),
    )
    address = models.CharField(max_length=200)
    phoneNumberRegex = RegexValidator(regex=r'^01([0|1|6|7|8|9]?)-?([0-9]{3,4})-?([0-9]{4})$')
    phone = models.CharField(validators=[phoneNumberRegex], max_length=11)
    gender = models.CharField(max_length=1, choices=GENDERS)

