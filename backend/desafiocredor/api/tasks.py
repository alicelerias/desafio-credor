import random

from celery import shared_task

from .models import Proposal


@shared_task
def process_proposal(proposal_id):
    print("Message received!")
    try:
        proposal_obj = Proposal.objects.get(id=proposal_id)
        approved = bool(random.randint(0, 1))
        proposal_obj.status = "approved" if approved else "denied"
        proposal_obj.save()
        print(f"Proposal {proposal_obj.status}")
    except Proposal.DoesNotExist:
        print("Proposal not found")
