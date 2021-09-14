import io

from fastapi import APIRouter, Path, UploadFile, File
from starlette.responses import StreamingResponse

from .models import engine, DBFile, DBFileResponse
from .config import SITE_DOMAIN

router = APIRouter()


@router.post("/upload", response_model=DBFileResponse)
async def upload_file(file: UploadFile = File(...)):
    db_file = DBFile(
        filename=file.filename,
        content_type=file.content_type,
        contents=await file.read()
    )
    await db_file.save_to_db()
    url = f"http://{SITE_DOMAIN}/f/{db_file.short_link}"
    return DBFileResponse(url=url)


@router.get("/f/{file_id}", response_class=StreamingResponse)
async def get_file(file_id: str = Path(..., regex="^[a-zA-Z0-9]{8}$")):
    model = await engine.find_one(DBFile, DBFile.short_link == file_id)
    return StreamingResponse(io.BytesIO(model.contents),
                             media_type=model.content_type)
