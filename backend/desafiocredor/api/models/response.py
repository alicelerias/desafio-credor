from django.db import models
from .proposal_fields import ProposalFields
from .proposal import Proposal

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
