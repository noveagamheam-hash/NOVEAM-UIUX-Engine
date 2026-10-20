from typing import Literal
from pydantic import BaseModel

class AIPersonalizationRequest(BaseModel):
    device: Literal["mobile", "tablet", "desktop"] = "desktop"
    theme: Literal["light", "dark", "system"] = "system"
    reduced_motion: bool = False
    high_contrast: bool = False
    experience_level: Literal["new", "returning", "regular"] = "new"

def recommend_experience(data: AIPersonalizationRequest):
    columns = {"mobile": 1, "tablet": 2, "desktop": 3}
    return {
        "engine": "NUX-10",
        "method": "rule_based",
        "device": data.device,
        "recommendations": {
            "theme": data.theme,
            "feed_columns": columns[data.device],
            "navigation": "bottom" if data.device == "mobile" else "top",
            "animations_enabled": not data.reduced_motion,
            "high_contrast": data.high_contrast,
            "show_onboarding": data.experience_level == "new",
            "feed_layout": "list" if data.device == "mobile" else "cards"
        }
    }
