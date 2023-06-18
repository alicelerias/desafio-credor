from django.db import models

from .mixins import TimestampedModel
from .proposal_fields import ProposalFields


class Proposal(TimestampedModel, models.Model):
    STATUS_CHOICES = (
        ("pending", "Pendente"),
        ("approved", "Aprovado"),
        ("denied", "Negado"),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self) -> str:
        return f"Proposal {self.id}"


class Response(models.Model):
    key = models.ForeignKey(
        ProposalFields,
        on_delete=models.PROTECT,
        related_name="responses",
        null=False,
    )
    value = models.TextField(null=False)
    proposal = models.ForeignKey(
        Proposal, on_delete=models.CASCADE, related_name="responses", null=False
    )

    def __str__(self) -> str:
        return f"Response"
