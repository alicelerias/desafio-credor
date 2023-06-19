import os
from celery import Celery

app = Celery("desafiocredor")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "desafiocredor.settings")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
