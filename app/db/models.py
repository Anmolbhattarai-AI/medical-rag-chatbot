from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.db.database import Base


class Document(Base):

    __tablename__ = "documents"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    filename = Column(
        String
    )

    chunk_strategy = Column(
        String
    )

    num_chunks = Column(
        Integer
    )


class InterviewBooking(Base):

    __tablename__ = "interview_bookings"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String
    )

    email = Column(
        String
    )

    date = Column(
        String
    )

    time = Column(
        String
    )