from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from components import api, tmp_video

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
app.include_router(tmp_video.router)