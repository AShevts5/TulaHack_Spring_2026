from fastapi import APIRouter
from pony.orm import db_session

router = APIRouter(tags=["health"])

@router.get("/health")
@db_session
def health() -> dict[str, str]:
    from db.models import TeamBuilderRecommendationRun

    TeamBuilderRecommendationRun.select().first()
    return {"status": "ok", "database": "reachable"}
