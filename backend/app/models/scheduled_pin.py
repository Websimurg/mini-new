from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, Text, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.database import Base

class ScheduledPin(Base):
    __tablename__ = "scheduled_pins"

    id = Column(Integer, primary_key=True, index=True)
    pin_id = Column(Integer, ForeignKey("pins.id"), nullable=False)
    content_plan_id = Column(Integer, ForeignKey("content_plans.id"), nullable=True)

    # Schedule
    scheduled_for = Column(DateTime, nullable=False, index=True)
    timezone = Column(String, default="UTC")

    # Status
    status = Column(String, default="pending")  # pending, processing, published, failed, cancelled
    retry_count = Column(Integer, default=0)
    max_retries = Column(Integer, default=3)

    # Error handling
    error_message = Column(Text, nullable=True)
    error_details = Column(JSON, default={})

    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    executed_at = Column(DateTime, nullable=True)

    # Relationships
    pin = relationship("Pin", back_populates="scheduled_pins")
    content_plan = relationship("ContentPlan", back_populates="scheduled_pins")
