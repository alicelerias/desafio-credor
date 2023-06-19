import os

from django.contrib.auth import get_user_model
from django.db.models.signals import post_migrate
from django.dispatch import receiver

User = get_user_model()


@receiver(post_migrate)
def create_superuser_on_startup(sender, **kwargs):
    print("SIGNAL ----------------!")
    if (
        "ADMIN_PASSWORD" in os.environ
        and not User.objects.filter(is_superuser=True).exists()
    ):
        User.objects.create_superuser(
            username="admin", password=os.environ["ADMIN_PASSWORD"], email=""
        )
        print("User admin created!")
