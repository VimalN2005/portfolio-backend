from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import ContactMessage
from schemas import ContactCreate, ContactResponse

router = APIRouter(prefix="/api/contact", tags=["Contact Inquiries"])

@router.post("", response_model=dict)
def submit_contact_message(
    payload: ContactCreate,
    db: Session = Depends(get_db)
):
    msg = ContactMessage(
        name=payload.name,
        email=payload.email,
        subject=payload.subject or "Portfolio Contact",
        message=payload.message
    )
    db.add(msg)
    db.commit()
    db.refresh(msg)

    return {
        "success": True,
        "message": "Thank you! Your message has been received.",
        "inquiry_id": msg.id
    }

@router.get("/messages")
def get_messages(db: Session = Depends(get_db)):
    msgs = db.query(ContactMessage).order_by(ContactMessage.created_at.desc()).all()
    return [{"id": m.id, "name": m.name, "email": m.email, "message": m.message, "date": m.created_at} for m in msgs]
