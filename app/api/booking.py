from fastapi import APIRouter

from app.db.database import SessionLocal

from app.services.booking import (
    create_booking
)

router = APIRouter()


@router.post("/book-interview")
def book_interview(
    name: str,
    email: str,
    date: str,
    time: str
):

    db = SessionLocal()

    booking = create_booking(
        db=db,
        name=name,
        email=email,
        date=date,
        time=time
    )

    db.close()

    return {
        "message": "Interview booked successfully",
        "booking_id": booking.id,
        "name": booking.name,
        "email": booking.email,
        "date": booking.date,
        "time": booking.time
    }