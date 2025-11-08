from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.database import Base

class PinterestAccount(Base):
    __tablename__ = "pinterest_accounts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # Pinterest credentials
    pinterest_user_id = Column(String, unique=True, index=True)
    username = Column(String)
    access_token = Column(String, nullable=False)
    refresh_token = Column(String)
    token_expires_at = Column(DateTime)

    # Account info
    profile_image = Column(String)
    bio = Column(String)
    website_url = Column(String)
    follower_count = Column(Integer, default=0)
    following_count = Column(Integer, default=0)
    monthly_views = Column(Integer, default=0)

    # Settings
    is_active = Column(Boolean, default=True)
    auto_pin_enabled = Column(Boolean, default=False)
    auto_schedule_enabled = Column(Boolean, default=False)

    # Automation settings
    automation_settings = Column(JSON, default={})  # Store complex settings

    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    last_synced_at = Column(DateTime, nullable=True)

    # Relationships
    user = relationship("User", back_populates="pinterest_accounts")
    boards = relationship("Board", back_populates="pinterest_account", cascade="all, delete-orphan")
    pins = relationship("Pin", back_populates="pinterest_account", cascade="all, delete-orphan")
    analytics = relationship("Analytics", back_populates="pinterest_account", cascade="all, delete-orphan")
