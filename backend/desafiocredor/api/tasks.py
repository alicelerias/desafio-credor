from celery import shared_task

from api.models import Proposal


@shared_task
def process_proposal():
    pass
