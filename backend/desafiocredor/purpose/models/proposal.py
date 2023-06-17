from django.db import models

from .mixins import TimestampedModel
from .customer import Customer


class Proposal(TimestampedModel, models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="proposals"
    )
    value = models.IntegerField()
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return str(self.value)
