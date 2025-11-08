from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)

    # Subscription
    subscription_tier = Column(String, default="free")  # free, basic, pro, enterprise
    subscription_expires_at = Column(DateTime, nullable=True)

    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationships
    pinterest_accounts = relationship("PinterestAccount", back_populates="user", cascade="all, delete-orphan")
    content_plans = relationship("ContentPlan", back_populates="user", cascade="all, delete-orphan")
    pins = relationship("Pin", back_populates="user", cascade="all, delete-orphan")
