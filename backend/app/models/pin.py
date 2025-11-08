from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Text, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.database import Base

class Pin(Base):
    __tablename__ = "pins"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    pinterest_account_id = Column(Integer, ForeignKey("pinterest_accounts.id"), nullable=False)
    board_id = Column(Integer, ForeignKey("boards.id"), nullable=True)

    # Pinterest pin info
    pinterest_pin_id = Column(String, unique=True, index=True, nullable=True)

    # Content
    title = Column(String, nullable=False)
    description = Column(Text)
    image_url = Column(String, nullable=False)
    local_image_path = Column(String, nullable=True)
    link = Column(String)  # Destination URL
    alt_text = Column(String)

    # SEO & Hashtags
    hashtags = Column(JSON, default=[])
    keywords = Column(JSON, default=[])

    # Status
    status = Column(String, default="draft")  # draft, scheduled, published, failed
    is_ai_generated = Column(Boolean, default=False)
    generation_metadata = Column(JSON, default={})  # AI generation details

    # Stats
    impressions = Column(Integer, default=0)
    saves = Column(Integer, default=0)
    clicks = Column(Integer, default=0)

    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    published_at = Column(DateTime, nullable=True)

    # Relationships
    user = relationship("User", back_populates="pins")
    pinterest_account = relationship("PinterestAccount", back_populates="pins")
    board = relationship("Board", back_populates="pins")
    scheduled_pins = relationship("ScheduledPin", back_populates="pin", cascade="all, delete-orphan")
