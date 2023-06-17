from django.db import models
from django.contrib.auth.models import User


from .mixins import TimestampedModel


class Customer(TimestampedModel, User, models.Model):
    name = models.CharField(max_length=150)
    cpf = models.IntegerField()
    adress = models.CharField(max_length=200)

    def __str__(self):
        return self.name
