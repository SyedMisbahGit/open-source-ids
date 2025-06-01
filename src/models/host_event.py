from datetime import datetime
from typing import Optional
from sqlalchemy import ForeignKey, String, JSON
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base

class HostEvent(Base):
    """Represents a host-based security event"""
    
    __tablename__ = "host_events"
    
    host_id: Mapped[str] = mapped_column(String(50), nullable=False)
    event_type: Mapped[str] = mapped_column(String(50), nullable=False)
    timestamp: Mapped[datetime] = mapped_column(nullable=False)
    data: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)
    
    def __repr__(self) -> str:
        return f"<HostEvent {self.host_id}: {self.event_type} ({self.timestamp})>"
    
    def to_dict(self) -> dict:
        base = super().to_dict()
        base["data"] = self.data or {}
        return base
