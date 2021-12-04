from fastapi import File, UploadFile, APIRouter
from fastapi.responses import FileResponse
from typing import List
some_file_path = "tfund_1637125005701.zip"
router = APIRouter()
@router.post("/")
async def up_fund(file: UploadFile = File(...)):
    # size = await file.read()
    return  { "report_ref": "tfund_1637125005701"}


@router.get("/download/{report_ref}", response_class=FileResponse)
async def get_ziptfund(report_ref: str):
    return some_file_path
