from fastapi import Depends, APIRouter, status
import sys
from function.NLPString_func import getNLP
from function.video_fusion import checkVideo

sys.path.append("..")
router = APIRouter(
    prefix="/api",
    tags=["api"],
)

@router.get("/")
def read_root():
    return checkVideo(['호박', '홍콩', '가마', '홍콩', '가마', '홍콩', '가마', '홍콩', '가마', '홍콩', '가마'])

@router.get("/data")
async def GetterDate(str: str = ''):
    return getNLP(str)