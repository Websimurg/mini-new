"""
Celery Tasks
Background jobs for automation
"""
from celery import Task
from app.celery_app import celery_app
from app.db.database import SessionLocal
from app.models.scheduled_pin import ScheduledPin
from app.models.pinterest_account import PinterestAccount
from app.models.content_plan import ContentPlan
from app.services.pinterest.pinterest_service import create_pinterest_service
from app.services.scheduler.scheduler_service import SchedulerService
from datetime import datetime, timedelta
import logging

logger = logging.getLogger(__name__)

class DatabaseTask(Task):
    """Base task with database session"""
    _db = None

    @property
    def db(self):
        if self._db is None:
            self._db = SessionLocal()
        return self._db

    def after_return(self, *args, **kwargs):
        if self._db is not None:
            self._db.close()
            self._db = None

@celery_app.task(base=DatabaseTask, bind=True)
def execute_scheduled_pins(self):
    """Execute all pending scheduled pins"""
    db = self.db
    scheduler_service = SchedulerService(db)

    try:
        # Get pending pins
        pending_pins = db.query(ScheduledPin).filter(
            ScheduledPin.status == "pending",
            ScheduledPin.scheduled_for <= datetime.utcnow()
        ).all()

        logger.info(f"Found {len(pending_pins)} pins to execute")

        for scheduled_pin in pending_pins:
            try:
                # Get Pinterest account
                pin = scheduled_pin.pin
                account = pin.pinterest_account

                # Create Pinterest service
                pinterest_service = create_pinterest_service(account.access_token)

                # Execute pin
                success = scheduler_service.execute_scheduled_pin(
                    scheduled_pin=scheduled_pin,
                    pinterest_service=pinterest_service
                )

                if success:
                    logger.info(f"Successfully executed scheduled pin {scheduled_pin.id}")
                else:
                    logger.error(f"Failed to execute scheduled pin {scheduled_pin.id}")

            except Exception as e:
                logger.error(f"Error executing scheduled pin {scheduled_pin.id}: {str(e)}")

    except Exception as e:
        logger.error(f"Error in execute_scheduled_pins task: {str(e)}")

@celery_app.task(base=DatabaseTask, bind=True)
def sync_pinterest_analytics(self):
    """Sync analytics from Pinterest for all accounts"""
    db = self.db

    try:
        # Get all active Pinterest accounts
        accounts = db.query(PinterestAccount).filter(
            PinterestAccount.is_active == True
        ).all()

        logger.info(f"Syncing analytics for {len(accounts)} accounts")

        for account in accounts:
            try:
                # Create Pinterest service
                pinterest_service = create_pinterest_service(account.access_token)

                # Get analytics for last 30 days
                end_date = datetime.utcnow()
                start_date = end_date - timedelta(days=30)

                analytics_data = pinterest_service.get_analytics(
                    start_date=start_date,
                    end_date=end_date
                )

                # Save to database
                # (Implementation depends on your analytics model structure)

                logger.info(f"Synced analytics for account {account.id}")

            except Exception as e:
                logger.error(f"Error syncing analytics for account {account.id}: {str(e)}")

    except Exception as e:
        logger.error(f"Error in sync_pinterest_analytics task: {str(e)}")

@celery_app.task(base=DatabaseTask, bind=True)
def process_rss_feeds(self):
    """Process RSS feeds from content plans"""
    db = self.db
    scheduler_service = SchedulerService(db)

    try:
        # Get active content plans with RSS feeds
        content_plans = db.query(ContentPlan).filter(
            ContentPlan.is_active == True,
            ContentPlan.source_type == "blog_rss"
        ).all()

        logger.info(f"Processing {len(content_plans)} RSS feeds")

        for plan in content_plans:
            try:
                # Fetch RSS feed
                articles = scheduler_service.fetch_rss_feed(plan.source_url)

                # Process each article
                # (Create pins, schedule them, etc.)
                # Implementation depends on your business logic

                # Update last executed time
                plan.last_executed_at = datetime.utcnow()
                db.commit()

                logger.info(f"Processed RSS feed for plan {plan.id}")

            except Exception as e:
                logger.error(f"Error processing RSS feed for plan {plan.id}: {str(e)}")

    except Exception as e:
        logger.error(f"Error in process_rss_feeds task: {str(e)}")

@celery_app.task(base=DatabaseTask, bind=True)
def cleanup_old_data(self):
    """Clean up old scheduled pins and analytics data"""
    db = self.db

    try:
        # Delete old completed scheduled pins (older than 90 days)
        cutoff_date = datetime.utcnow() - timedelta(days=90)

        deleted = db.query(ScheduledPin).filter(
            ScheduledPin.status.in_(["published", "failed"]),
            ScheduledPin.executed_at < cutoff_date
        ).delete()

        db.commit()

        logger.info(f"Cleaned up {deleted} old scheduled pins")

    except Exception as e:
        logger.error(f"Error in cleanup_old_data task: {str(e)}")

@celery_app.task(bind=True)
def generate_ai_content_batch(self, pin_ids: list):
    """Generate AI content for multiple pins"""
    # Implementation for batch AI content generation
    logger.info(f"Generating AI content for {len(pin_ids)} pins")
    # Add your implementation here
