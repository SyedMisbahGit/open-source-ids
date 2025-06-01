from datetime import datetime
from typing import List
from sqlalchemy import ForeignKey, String, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base

class Signature(Base):
    """Represents a signature rule in the IDS system"""
    
    __tablename__ = "signatures"
    
    signature_id: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    category: Mapped[str] = mapped_column(String(50), nullable=False)
    severity: Mapped[int] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rule: Mapped[str] = mapped_column(String(1000), nullable=False)
    metadata: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)
    
    # Relationships
    alerts: Mapped[List["Alert"]] = relationship("Alert", back_populates="signature")
    
    def __repr__(self) -> str:
        return f"<Signature {self.signature_id}: {self.category} ({self.severity})>"
    
    def to_dict(self) -> dict:
        base = super().to_dict()
        base["metadata"] = self.metadata or {}
        return base
