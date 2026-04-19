from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.lifespan import lifespan
from app.routers import health, team_builder

app = FastAPI(title="Team Builder API", lifespan=lifespan)

_origins = settings.cors_origins_list
_creds = "*" not in _origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=_origins if _origins else ["*"],
    allow_credentials=_creds,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router)
app.include_router(team_builder.router)
