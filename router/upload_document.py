from fastapi import APIRouter, Form, File, HTTPException, FastAPI
from models.verify import DbUser, DbUpload



router = APIRouter(
    prefix="/uploadDocument",
    tags=["/Upload Document"]
)

@router.post("/uploaddocument")
def upload_document(
    document :str=File(...),

)
