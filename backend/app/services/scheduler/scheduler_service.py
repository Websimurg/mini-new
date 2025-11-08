"""
Content Scheduler Service
Handles content scheduling and automation (BlogToPin features)
"""
from typing import Optional, Dict, List
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from app.models.scheduled_pin import ScheduledPin
from app.models.pin import Pin
from app.services.pinterest.pinterest_service import PinterestService
import feedparser
import httpx
from bs4 import BeautifulSoup

class SchedulerService:
    def __init__(self, db: Session):
        self.db = db

    async def schedule_pin(
        self,
        pin_id: int,
        scheduled_for: datetime,
        content_plan_id: Optional[int] = None,
        timezone: str = "UTC"
    ) -> ScheduledPin:
        """Schedule a pin for publishing"""

        scheduled_pin = ScheduledPin(
            pin_id=pin_id,
            content_plan_id=content_plan_id,
            scheduled_for=scheduled_for,
            timezone=timezone,
            status="pending"
        )

        self.db.add(scheduled_pin)
        self.db.commit()
        self.db.refresh(scheduled_pin)

        return scheduled_pin

    async def get_pending_pins(
        self,
        before: Optional[datetime] = None
    ) -> List[ScheduledPin]:
        """Get pins scheduled to be published"""

        if before is None:
            before = datetime.utcnow()

        return self.db.query(ScheduledPin).filter(
            ScheduledPin.status == "pending",
            ScheduledPin.scheduled_for <= before
        ).all()

    async def execute_scheduled_pin(
        self,
        scheduled_pin: ScheduledPin,
        pinterest_service: PinterestService
    ) -> bool:
        """Execute a scheduled pin (publish to Pinterest)"""

        try:
            scheduled_pin.status = "processing"
            self.db.commit()

            # Get pin details
            pin = self.db.query(Pin).filter(Pin.id == scheduled_pin.pin_id).first()

            if not pin:
                raise ValueError(f"Pin {scheduled_pin.pin_id} not found")

            # Upload to Pinterest
            result = await pinterest_service.create_pin(
                board_id=pin.board.pinterest_board_id,
                title=pin.title,
                description=pin.description,
                image_url=pin.image_url,
                link=pin.link,
                alt_text=pin.alt_text
            )

            # Update pin with Pinterest ID
            pin.pinterest_pin_id = result.get("id")
            pin.status = "published"
            pin.published_at = datetime.utcnow()

            # Update scheduled pin
            scheduled_pin.status = "published"
            scheduled_pin.executed_at = datetime.utcnow()

            self.db.commit()
            return True

        except Exception as e:
            # Handle errors
            scheduled_pin.status = "failed"
            scheduled_pin.error_message = str(e)
            scheduled_pin.retry_count += 1

            # Retry if under max retries
            if scheduled_pin.retry_count < scheduled_pin.max_retries:
                scheduled_pin.status = "pending"
                scheduled_pin.scheduled_for = datetime.utcnow() + timedelta(minutes=15)

            self.db.commit()
            return False

    async def fetch_rss_feed(self, feed_url: str) -> List[Dict]:
        """Fetch and parse RSS feed (BlogToPin feature)"""

        feed = feedparser.parse(feed_url)
        articles = []

        for entry in feed.entries[:10]:  # Get last 10 articles
            article = {
                "title": entry.get("title", ""),
                "link": entry.get("link", ""),
                "description": entry.get("description", ""),
                "published": entry.get("published", ""),
                "image": None
            }

            # Try to extract image
            if "media_content" in entry:
                article["image"] = entry.media_content[0].get("url")
            elif "enclosures" in entry:
                for enclosure in entry.enclosures:
                    if "image" in enclosure.get("type", ""):
                        article["image"] = enclosure.get("href")
                        break

            articles.append(article)

        return articles

    async def convert_blog_to_pin(
        self,
        blog_url: str
    ) -> Dict:
        """Convert blog post to pin content (BlogToPin feature)"""

        async with httpx.AsyncClient() as client:
            response = await client.get(blog_url)
            html = response.text

        soup = BeautifulSoup(html, "lxml")

        # Extract content
        title = soup.find("h1")
        title_text = title.get_text() if title else ""

        # Extract meta description
        meta_desc = soup.find("meta", {"name": "description"})
        description = meta_desc.get("content", "") if meta_desc else ""

        # Extract main image
        og_image = soup.find("meta", {"property": "og:image"})
        image_url = og_image.get("content", "") if og_image else None

        if not image_url:
            # Fallback to first img tag
            img = soup.find("img")
            image_url = img.get("src", "") if img else None

        return {
            "title": title_text,
            "description": description,
            "image_url": image_url,
            "source_url": blog_url
        }

    async def generate_schedule_times(
        self,
        frequency: str,
        start_date: datetime,
        count: int = 30,
        preferred_times: Optional[List[str]] = None
    ) -> List[datetime]:
        """Generate optimal posting schedule"""

        if preferred_times is None:
            # Default best times for Pinterest (based on research)
            preferred_times = ["09:00", "14:00", "20:00"]

        schedule = []
        current_date = start_date

        if frequency == "daily":
            for i in range(count):
                for time_str in preferred_times:
                    hour, minute = map(int, time_str.split(":"))
                    scheduled_time = current_date.replace(hour=hour, minute=minute)
                    schedule.append(scheduled_time)

                current_date += timedelta(days=1)

        elif frequency == "weekly":
            # Post on specific days (Mon, Wed, Fri)
            posting_days = [0, 2, 4]  # Monday, Wednesday, Friday

            while len(schedule) < count:
                if current_date.weekday() in posting_days:
                    for time_str in preferred_times:
                        hour, minute = map(int, time_str.split(":"))
                        scheduled_time = current_date.replace(hour=hour, minute=minute)
                        schedule.append(scheduled_time)

                current_date += timedelta(days=1)

        return schedule[:count]

    async def bulk_schedule_pins(
        self,
        pin_ids: List[int],
        start_date: datetime,
        frequency: str = "daily",
        preferred_times: Optional[List[str]] = None
    ) -> List[ScheduledPin]:
        """Bulk schedule multiple pins"""

        schedule_times = await self.generate_schedule_times(
            frequency=frequency,
            start_date=start_date,
            count=len(pin_ids),
            preferred_times=preferred_times
        )

        scheduled_pins = []

        for pin_id, scheduled_time in zip(pin_ids, schedule_times):
            scheduled_pin = await self.schedule_pin(
                pin_id=pin_id,
                scheduled_for=scheduled_time
            )
            scheduled_pins.append(scheduled_pin)

        return scheduled_pins
