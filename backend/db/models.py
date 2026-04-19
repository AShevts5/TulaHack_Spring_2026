from datetime import datetime, timezone
from pony.orm import Json, Optional, PrimaryKey, Required
from .database import db

def _utc_now() -> datetime:
    return datetime.now(timezone.utc)

class TeamBuilderRecommendationRun(db.Entity):
    _table_ = "team_builder_recommendation_runs"

    id = PrimaryKey(int, auto=True)
    created_at = Required(datetime, default=_utc_now)
    mode = Optional(str)  
    preset_key = Optional(str)
    criterium = Required(Json)
    result = Required(Json)
    user_id = Optional(int)


class TeamBuilderSavedProfile(db.Entity):

    _table_ = "team_builder_saved_profiles"

    id = PrimaryKey(int, auto=True)
    created_at = Required(datetime, default=_utc_now)
    title = Required(str)
    criterium = Required(Json)
    user_id = Optional(int)
