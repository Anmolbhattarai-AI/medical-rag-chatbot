from sqlalchemy.orm import Session

from app.db.models import InterviewBooking


def create_booking(
    db: Session,
    name: str,
    email: str,
    date: str,
    time: str
):

    booking = InterviewBooking(
        name=name,
        email=email,
        date=date,
        time=time
    )

    db.add(booking)

    db.commit()

    db.refresh(booking)

    return booking