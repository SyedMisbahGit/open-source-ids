from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.ext.declarative import declarative_base
from contextlib import contextmanager
from typing import Generator
import logging
from src.config.suricata import SURICATA_CONFIG

logger = logging.getLogger(__name__)

# Create base classes
Base = declarative_base()

# Create database engine
engine = create_engine(SURICATA_CONFIG.get('DATABASE_URL', 'sqlite:///ids_data.db'))

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@contextmanager
def get_db() -> Generator:
    """Get database session using context manager"""
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        logger.error(f"Database error: {str(e)}")
        db.rollback()
        raise
    finally:
        db.close()

def init_db() -> None:
    """Initialize database and create tables"""
    try:
        Base.metadata.create_all(bind=engine)
        logger.info("Database tables created successfully")
    except Exception as e:
        logger.error(f"Error initializing database: {str(e)}")
        raise

def get_session():
    """Get database session"""
    return SessionLocal()
