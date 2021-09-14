import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from . import routes
from .models import engine, ShortLinkIndex

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    if index_model := await engine.find_one(ShortLinkIndex) is None:
        await ShortLinkIndex.init_index()


app.include_router(routes.router)
