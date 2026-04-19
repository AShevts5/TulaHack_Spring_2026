from datetime import datetime
from typing import Literal
from pydantic import BaseModel, Field

class RecommendRequest(BaseModel):
    mode: Literal["hire", "team"] = "hire"
    role: str = Field(..., min_length=1, max_length=255, examples=["Аналитик"])
    disc: dict[str, int] = Field(
        ...,
        description="Проценты D, I, S, C (сумма может быть ≠100 — нормализуем в сервисе).",
        examples=[{"D": 30, "I": 20, "S": 35, "C": 15}],
    )
    motivation: list[str] = Field(default_factory=list)
    generation: str | None = Field(None, max_length=64)
    team_context: str | None = None
    manager_notes: str | None = None
    preset_key: str | None = Field(None, max_length=64)
    user_id: int | None = None

class RecommendResponse(BaseModel):
    id: int
    mode: str | None
    criteria: dict
    result: dict
    created_at: datetime

class SavedProfileCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    criteria: dict
    user_id: int | None = None

class SavedProfileResponse(BaseModel):
    id: int
    title: str
    criteria: dict
    created_at: datetime
