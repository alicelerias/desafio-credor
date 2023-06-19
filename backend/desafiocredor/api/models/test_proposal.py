from django.test import TestCase

from .proposal import Proposal


class TestProposal(TestCase):
    """Test module for Proposal model"""

    def setUp(self) -> None:
        self.proposal_1 = Proposal.objects.create(status="pending")
        self.proposal_2 = Proposal.objects.create(status="denied")
        self.proposal_1.save()
        self.proposal_2.save()

    def test_proposal_model(self):
        proposal = Proposal.objects.get(pk="1")
        self.assertEqual(proposal.status, "pending")
