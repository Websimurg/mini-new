from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.database import Base

class Board(Base):
    __tablename__ = "boards"

    id = Column(Integer, primary_key=True, index=True)
    pinterest_account_id = Column(Integer, ForeignKey("pinterest_accounts.id"), nullable=False)

    # Pinterest board info
    pinterest_board_id = Column(String, unique=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    privacy = Column(String, default="public")  # public, protected, secret

    # Board stats
    pin_count = Column(Integer, default=0)
    follower_count = Column(Integer, default=0)

    # Board image
    image_url = Column(String)

    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationships
    pinterest_account = relationship("PinterestAccount", back_populates="boards")
    pins = relationship("Pin", back_populates="board", cascade="all, delete-orphan")
