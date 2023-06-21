from django.db import models

from .proposal_field import ProposalField
from .proposal import Proposal


class Response(models.Model):
    key = models.ForeignKey(
        ProposalField,
        on_delete=models.PROTECT,
        related_name="responses",
        null=False,
    )
    value = models.TextField(null=True, blank=True)
    proposal = models.ForeignKey(
        Proposal, on_delete=models.CASCADE, related_name="responses", null=False
    )

    def __str__(self) -> str:
        return f"Response"
