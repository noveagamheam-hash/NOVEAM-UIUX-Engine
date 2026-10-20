from typing import Literal
from pydantic import BaseModel

class PWARequest(BaseModel):
    device: Literal["mobile", "tablet", "desktop"] = "desktop"
    online: bool = True
    installed: bool = False

def get_pwa_experience(data: PWARequest):
    return {
        "device": data.device,
        "connection": "online" if data.online else "offline",
        "installed": data.installed,
        "experience": {
            "show_install_prompt": data.online and not data.installed,
            "show_offline_notice": not data.online,
            "offline_page": "/offline.html",
            "start_page": "/welcome.html",
            "cache_strategy": "service_worker_managed"
        }
    }
