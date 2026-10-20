from typing import Literal
from pydantic import BaseModel

NAV_ITEMS = [
    {"id": "home", "label": "Home", "path": "/feed.html"},
    {"id": "explore", "label": "Explore", "path": "/explore.html"},
    {"id": "community", "label": "Community", "path": "/community.html"},
    {"id": "portfolio", "label": "Portfolio", "path": "/portfolio.html"},
    {"id": "profile", "label": "Profile", "path": "/profile.html"}
]

class NavigationRequest(BaseModel):
    device: Literal["mobile", "tablet", "desktop"] = "desktop"
    active_page: Literal["home", "explore", "community", "portfolio", "profile"] = "home"

def get_navigation(data: NavigationRequest):
    return {
        "device": data.device,
        "position": "bottom" if data.device == "mobile" else "top",
        "items": [
            {**item, "active": item["id"] == data.active_page}
            for item in NAV_ITEMS
        ]
    }
