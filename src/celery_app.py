from celery import Celery
from celery.schedules import crontab

from src.config import settings


celery_app = Celery(
    settings.celery_settings.celery_app_name,
    broker=settings.celery_settings.celery_broker_url,
    backend=settings.celery_settings.celery_backend_url,
)

celery_app.conf.timezone = "UTC"

celery_app.conf.beat_schedule = {
    "call-scheduled-endpoint-every-minute": {
        "task": "src.api.router.call_scheduled_endpoint",
        "schedule": crontab(minute="*"),
    },
}