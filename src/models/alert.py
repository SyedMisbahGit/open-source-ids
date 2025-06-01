from datetime import datetime
from typing import Optional
from sqlalchemy import ForeignKey, String, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base

class Alert(Base):
    """Represents a network security alert"""
    
    __tablename__ = "alerts"
    
    timestamp: Mapped[datetime] = mapped_column(nullable=False)
    source_ip: Mapped[str] = mapped_column(String(15), nullable=False)
    dest_ip: Mapped[str] = mapped_column(String(15), nullable=False)
    source_port: Mapped[Optional[int]] = mapped_column(nullable=True)
    dest_port: Mapped[Optional[int]] = mapped_column(nullable=True)
    protocol: Mapped[Optional[str]] = mapped_column(String(10), nullable=True)
    category: Mapped[str] = mapped_column(String(50), nullable=False)
    signature: Mapped[str] = mapped_column(String(255), nullable=False)
    severity: Mapped[int] = mapped_column(nullable=False)
    additional_data: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)
    
    # Relationships
    signature_id: Mapped[int] = mapped_column(ForeignKey("signatures.id"), nullable=True)
    signature: Mapped["Signature"] = relationship("Signature", back_populates="alerts")
    
    def __repr__(self) -> str:
        return f"<Alert {self.id}: {self.source_ip} -> {self.dest_ip} ({self.category})>"
    
    def to_dict(self) -> dict:
        base = super().to_dict()
        base["additional_data"] = self.additional_data or {}
        return base
