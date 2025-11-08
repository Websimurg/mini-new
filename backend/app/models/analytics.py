from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Date, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.database import Base

class Analytics(Base):
    __tablename__ = "analytics"

    id = Column(Integer, primary_key=True, index=True)
    pinterest_account_id = Column(Integer, ForeignKey("pinterest_accounts.id"), nullable=False)

    # Date for analytics
    date = Column(Date, nullable=False, index=True)

    # Metrics
    impressions = Column(Integer, default=0)
    saves = Column(Integer, default=0)
    clicks = Column(Integer, default=0)
    pin_clicks = Column(Integer, default=0)
    outbound_clicks = Column(Integer, default=0)

    # Engagement
    engagement_rate = Column(Integer, default=0)  # Stored as percentage * 100

    # Followers
    new_followers = Column(Integer, default=0)
    unfollowers = Column(Integer, default=0)
    total_followers = Column(Integer, default=0)

    # Top performing content
    top_pins = Column(JSON, default=[])
    top_boards = Column(JSON, default=[])

    # Audience insights
    audience_demographics = Column(JSON, default={})
    audience_interests = Column(JSON, default={})

    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationships
    pinterest_account = relationship("PinterestAccount", back_populates="analytics")
