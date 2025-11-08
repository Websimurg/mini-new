from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, JSON, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.database import Base

class ContentPlan(Base):
    __tablename__ = "content_plans"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # Plan details
    name = Column(String, nullable=False)
    description = Column(Text)

    # Content source
    source_type = Column(String)  # blog_rss, manual, ai_generated, url
    source_url = Column(String, nullable=True)  # RSS feed URL or blog URL

    # Schedule settings
    frequency = Column(String)  # daily, weekly, custom
    schedule_config = Column(JSON, default={})  # Custom schedule times

    # Content settings
    content_config = Column(JSON, default={})  # AI prompts, templates, etc.

    # Status
    is_active = Column(Boolean, default=True)

    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    last_executed_at = Column(DateTime, nullable=True)
    next_execution_at = Column(DateTime, nullable=True)

    # Relationships
    user = relationship("User", back_populates="content_plans")
    scheduled_pins = relationship("ScheduledPin", back_populates="content_plan", cascade="all, delete-orphan")
