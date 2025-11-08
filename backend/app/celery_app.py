"""
Celery Application
Handles background tasks and scheduling
"""
from celery import Celery
from celery.schedules import crontab
from app.core.config import settings

celery_app = Celery(
    "pinterest_growth",
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND,
    include=["app.tasks"]
)

# Celery configuration
celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
    task_track_started=True,
    task_time_limit=30 * 60,  # 30 minutes
    task_soft_time_limit=25 * 60,  # 25 minutes
)

# Periodic tasks
celery_app.conf.beat_schedule = {
    # Check and execute scheduled pins every 5 minutes
    "execute-scheduled-pins": {
        "task": "app.tasks.execute_scheduled_pins",
        "schedule": crontab(minute="*/5"),
    },
    # Sync Pinterest analytics daily at 2 AM
    "sync-pinterest-analytics": {
        "task": "app.tasks.sync_pinterest_analytics",
        "schedule": crontab(hour=2, minute=0),
    },
    # Process RSS feeds every hour
    "process-rss-feeds": {
        "task": "app.tasks.process_rss_feeds",
        "schedule": crontab(minute=0),
    },
    # Clean up old data weekly
    "cleanup-old-data": {
        "task": "app.tasks.cleanup_old_data",
        "schedule": crontab(day_of_week=0, hour=3, minute=0),
    },
}
