from typing import Literal
from pydantic import BaseModel

class FeedRequest(BaseModel):
    device: Literal["mobile", "tablet", "desktop"] = "desktop"
    layout: Literal["list", "cards", "compact"] = "cards"
    mode: Literal["personalized", "following", "chronological"] = "personalized"
    reduced_motion: bool = False

def get_feed_presentation(data: FeedRequest):
    columns = {"mobile": 1, "tablet": 2, "desktop": 3}
    return {
        "device": data.device,
        "layout": data.layout,
        "mode": data.mode,
        "presentation": {
            "columns": columns[data.device],
            "animations_enabled": not data.reduced_motion,
            "show_sidebar": data.device == "desktop"
        }
    }
