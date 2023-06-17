from django.db import models

from mixins import TimestampedModel


class Purpose(TimestampedModel, models.Model):
    value = models.IntegerField(max_length=11)
    accepted = models.BooleanField()
    def __str__(self):
        return self.value
