from typing import Literal
from pydantic import BaseModel, Field

class AnalyticsEvent(BaseModel):
    event: Literal["page_view", "navigation_click", "pwa_install", "feedback_open", "onboarding_complete"]
    page: str = Field(default="/", max_length=200)
    device: Literal["mobile", "tablet", "desktop"] = "desktop"

def validate_analytics_event(data: AnalyticsEvent):
    return {
        "status": "validated",
        "event": data.event,
        "page": data.page,
        "device": data.device,
        "saved": False
    }
