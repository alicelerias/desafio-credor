from django.db import models

from mixins import TimestampedModel


class Customer(TimestampedModel, models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    cpf = models.IntegerField(max_length=11)
    adress = models.CharField(max_length=200)

    def __str__(self):
        return self.name
