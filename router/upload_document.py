from alembic.command import current
from fastapi import APIRouter, Form, File, HTTPException, FastAPI, Depends, UploadFile
from models.verify import DbUser, DbUpload
from sqlalchemy.orm import Session
from router.user import get_current_user
from database.db import get_db
import os
import shutil

router = APIRouter(prefix="/uploadDocument", tags=["/Upload Document"])

folder = "Documents/"

os.makedirs(folder, exist_ok=True)


@router.post("/uploaddocument")
def upload_document(
    document: UploadFile = File(...),
    username: str = Form(...),
    current_user: DbUser = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    user = db.query(DbUser).filter(DbUser.id == current_user.id).first()

    if not user:
        raise HTTPException(status_code=400, detail="User not found.")

    file_path = os.path.join(folder, document.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(document.file, buffer)

    try:
        new_request = DbUpload(
            user_id=user.id,
            document=file_path,
            username=username,
        )

        db.add(new_request)
        db.commit()
        db.refresh(new_request)

        return {
            "message": f"Document of {username} is successfully upload .It is apporve by admin"
        }
    except Exception as e:
        db.rollback()
        print("Error", repr(e))
        raise HTTPException(status_code=400, detail="Document upload request is failed")
