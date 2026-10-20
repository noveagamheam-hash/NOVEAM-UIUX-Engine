from typing import Literal
from pydantic import BaseModel, Field

class UXPreferences(BaseModel):
    theme: Literal["light", "dark", "system"] = "system"
    font_scale: float = Field(default=1.0, ge=0.8, le=2.0)
    reduced_motion: bool = False
    high_contrast: bool = False
    feed_layout: Literal["list", "cards", "compact"] = "cards"

def get_default_preferences():
    return UXPreferences()

def preview_preferences(preferences: UXPreferences):
    return {
        "status": "valid",
        "preferences": preferences.model_dump()
    }
