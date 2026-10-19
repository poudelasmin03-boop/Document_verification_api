import enum
from datetime import UTC, datetime
from re import L
from database.db import Base
from sqlalchemy import (
    Boolean,
    Column,
    VARCHAR,
    DateTime,
    Enum,
    Float,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship


class DbUser(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)
    create_at = Column(DateTime(timezone=True), default=lambda: datetime.now(UTC))


### Document Upload


class DbUpload(Base):
    __tablename__ = "Document_upload"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    document = Column(VARCHAR(300), nullable=False)
    user_id = Column(Integer, ForeignKey("Users.id"))
