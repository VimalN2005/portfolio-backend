import os
import uuid
from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import UploadedMedia

router = APIRouter(prefix="/api/upload", tags=["Media Upload"])

UPLOAD_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "static", "uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)

ALLOWED_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".svg"}
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB

@router.post("")
async def upload_file(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    # Extension validation
    ext = os.path.splitext(file.filename)[1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid file type '{ext}'. Allowed: {', '.join(ALLOWED_EXTENSIONS)}"
        )

    # Read content & check size
    content = await file.read()
    if len(content) > MAX_FILE_SIZE:
        raise HTTPException(status_code=400, detail="File too large (Max 10MB)")

    # Unique filename
    unique_name = f"{uuid.uuid4().hex[:12]}_{file.filename}"
    filepath = os.path.join(UPLOAD_DIR, unique_name)

    # Save to disk
    with open(filepath, "wb") as f:
        f.write(content)

    file_url = f"/static/uploads/{unique_name}"

    # Save record to DB
    media_entry = UploadedMedia(
        filename=file.filename,
        file_url=file_url,
        content_type=file.content_type or "image/png"
    )
    db.add(media_entry)
    db.commit()
    db.refresh(media_entry)

    return {
        "success": True,
        "message": "File uploaded successfully",
        "media_id": media_entry.id,
        "filename": unique_name,
        "url": file_url
    }
