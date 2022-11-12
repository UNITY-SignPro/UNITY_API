from fastapi import Depends, APIRouter, status
import sys
# from function.NLPString import getNLP
from function.NLPString import getNLP
#
from pydantic import BaseModel
from typing import Optional




sys.path.append("..")
router = APIRouter(
    prefix="/api",
    tags=["api"],
    # responses={401: {"user": "Not authorized"}},
)

@router.get("/data")
async def GetterDate(query: str = ''):
    return getNLP(query)
    return "SelectData(query)"