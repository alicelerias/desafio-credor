import json

from django.core.management.base import BaseCommand
from django.core.serializers import deserialize
from ...models import ProposalField


SEED_DATA = "./api/management/commands/seed_data.json"


class Command(BaseCommand):
    help = "Seed the database with initial data"

    def handle(self, *args, **options):
        # Load seed data from SEED_DATA
        with open(SEED_DATA) as f:
            seed_data = json.load(f)

        # Delete existing data
        ProposalField.objects.all().delete()

        # Create objects from the seed data
        for obj in seed_data:
            ProposalField.objects.create(**obj)

        self.stdout.write(self.style.SUCCESS("Data seeded successfully."))
