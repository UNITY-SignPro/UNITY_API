import json
import os
from typing import Optional

from fastapi import Depends, APIRouter, status
from fastapi.responses import ORJSONResponse
import sys
from fastapi.responses import StreamingResponse


sys.path.append("..")
router = APIRouter(
    prefix="/tmp_video",
    tags=["tmp_video"],
)

__videopath__ = os.path.abspath(f'C:/Users/dlalsdn/Desktop/Project/TeamUnity_Back/tmp_video/what.avi')

@router.get("/")
def main():
    def iterfile():
        with open(__videopath__, mode="rb") as file_like:
            yield from file_like

    return StreamingResponse(iterfile(), media_type="video/mp4")