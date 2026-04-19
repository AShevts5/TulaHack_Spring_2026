import json
from pathlib import Path
from fastapi import APIRouter, HTTPException
from pony.orm import db_session, select

from app.schemas.team_builder import (
    RecommendRequest,
    RecommendResponse,
    SavedProfileCreate,
    SavedProfileResponse,
)
from app.services.recommendations import build_recommendations
from db.models import TeamBuilderRecommendationRun, TeamBuilderSavedProfile

router = APIRouter(prefix="/api/team-builder", tags=["team-builder"])

_PRESETS_PATH = Path(__file__).resolve().parent.parent / "data" / "presets.json"

@router.get("/presets")
def list_presets() -> list[dict]:
    if not _PRESETS_PATH.is_file():
        return []
    with _PRESETS_PATH.open(encoding="utf-8") as f:
        return json.load(f)


@router.post("/recommendations", response_model=RecommendResponse)
@db_session
def create_recommendation(body: RecommendRequest) -> RecommendResponse:
    criteria = body.model_dump()
    result = build_recommendations(criteria)
    run = TeamBuilderRecommendationRun(
        mode=criteria.get("mode"),
        preset_key=criteria.get("preset_key"),
        criteria=criteria,
        result=result,
        user_id=criteria.get("user_id"),
    )
    return RecommendResponse(
        id=run.id,
        mode=run.mode,
        criteria=run.criteria,
        result=run.result,
        created_at=run.created_at,
    )


@router.get("/recommendations/{run_id}", response_model=RecommendResponse)
@db_session
def get_recommendation(run_id: int) -> RecommendResponse:
    run = select(r for r in TeamBuilderRecommendationRun if r.id == run_id).first()
    if run is None:
        raise HTTPException(status_code=404, detail="run_not_found")
    return RecommendResponse(
        id=run.id,
        mode=run.mode,
        criteria=run.criteria,
        result=run.result,
        created_at=run.created_at,
    )


@router.post("/saved-profiles", response_model=SavedProfileResponse)
@db_session
def create_saved_profile(body: SavedProfileCreate) -> SavedProfileResponse:
    row = TeamBuilderSavedProfile(
        title=body.title,
        criteria=body.criteria,
        user_id=body.user_id,
    )
    return SavedProfileResponse(
        id=row.id,
        title=row.title,
        criteria=row.criteria,
        created_at=row.created_at,
    )


@router.get("/saved-profiles", response_model=list[SavedProfileResponse])
@db_session
def list_saved_profiles() -> list[SavedProfileResponse]:
    rows = list(TeamBuilderSavedProfile.select())
    rows.sort(key=lambda r: r.id, reverse=True)
    rows = rows[:50]
    return [
        SavedProfileResponse(id=r.id, title=r.title, criteria=r.criteria, created_at=r.created_at)
        for r in rows
    ]
