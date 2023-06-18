from django.db import models

from .mixins import TimestampedModel


class ProposalFields(TimestampedModel, models.Model):
    FORM_CHOICES = (
        ("string", "Texto"),
        ("number", "Número"),
    )

    name = models.CharField(
        primary_key=True, max_length=20, null=False, blank=False
    )
    type = models.CharField(
        max_length=10, choices=FORM_CHOICES, null=False, default="string"
    )
    nullable = models.BooleanField(default=True)
    order = models.FloatField()

    def __str__(self) -> str:
        return f"Campo: {self.name}"
