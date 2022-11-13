import json
from typing import Optional

from fastapi import Depends, APIRouter, status
import sys

from pydantic import BaseModel

from function.NLPString_func import getNLP
from function.video_fusion import checkVideo

sys.path.append("..")
router = APIRouter(
    prefix="/api",
    tags=["api"],
)



class WordModel(BaseModel):
    words: list

# 추가 필요
@router.get("/model")
def read_root(str: str = ''):
    return checkVideo(str.split(', '))

@router.get("/translate")
async def GetterDate(str: str = ''):
    return getNLP(str)