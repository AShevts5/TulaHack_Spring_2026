from functools import lru_cache
from app.config import Settings, get_settings

@lru_cache
def settings_dependency() -> Settings:
    return get_settings()
