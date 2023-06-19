import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

User = get_user_model()


class Command(BaseCommand):
    help = "Create a superuser if ADMIN_PASSWORD environment variable is available"

    def handle(self, *args, **options):
        admin_password = os.environ.get("ADMIN_PASSWORD")
        if not admin_password and User.objects.filter(username="admin").exists():
            return

        User.objects.create_superuser(
            username="admin", password=admin_password, email=""
        )
        self.stdout.write(self.style.SUCCESS("Superuser created successfully."))
