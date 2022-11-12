from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from components import api
# from function.NLPString import getNLP

app = FastAPI()
# CORS 해결
origins = [
    "http://localhost",
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api.router)

# # root page
# @app.get("/")
# def read_root():
#     return "welcome to the unity api server"
#
# @app.get("/translate")
# async def translate(str: str = ""):
#     return getNLP(str)