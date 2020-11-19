from __future__ import absolute_import
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eshop.settings')

celery_app = Celery('eshop')

celery_app.config_from_object('django.conf:settings', namespace="CELERY")
celery_app.autodiscover_tasks()

celery_app.conf.beat_schedule = {
    "test cron task": {
        "task": "main.tasks.test",
        "schedule": 10.0,  # seconds
        "args": ("Hellosd",)
    }
}

celery_app.conf.timezone = "UTC"

# to start bg worker
# celery -A eshop beat -l info
