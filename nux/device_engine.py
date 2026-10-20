from fastapi import APIRouter
from pydantic import BaseModel, Field
from typing import List, Literal

router = APIRouter(
    prefix="/api/ux/device",
    tags=["NUX-11 Universal Devices"]
)

class DeviceProfile(BaseModel):
    device_type: Literal[
        "desktop", "mobile", "tablet", "foldable",
        "smart_tv", "smartwatch", "console",
        "handheld_console", "cloud_console",
        "vr", "ar", "mr", "smart_display", "other"
    ]
    screen_width: int = Field(ge=1, le=16384)
    screen_height: int = Field(ge=1, le=16384)
    input_methods: List[str] = Field(default_factory=list)
    reduced_motion: bool = False
    high_contrast: bool = False

@router.post("/adapt")
def adapt_device(profile: DeviceProfile):
    device = profile.device_type

    if device in ("smart_tv", "console", "cloud_console"):
        layout, navigation, columns = "ten_foot", "directional_focus", 4
    elif device == "smartwatch":
        layout, navigation, columns = "compact", "minimal", 1
    elif device in ("vr", "ar", "mr"):
        layout, navigation, columns = "spatial", "spatial_input", 1
    elif device == "handheld_console":
        layout, navigation, columns = "hybrid", "gamepad_touch", 2
    elif device == "mobile":
        layout, navigation, columns = "mobile", "bottom", 1
    elif device in ("tablet", "foldable"):
        layout, navigation, columns = "adaptive", "side_or_bottom", 2
    else:
        layout, navigation, columns = "desktop", "sidebar", 3

    return {
        "engine": "NUX-11",
        "device_type": device,
        "layout": layout,
        "navigation": navigation,
        "feed_columns": columns,
        "input_methods": profile.input_methods,
        "animations_enabled": not profile.reduced_motion,
        "high_contrast": profile.high_contrast,
        "touch_friendly": "touch" in profile.input_methods,
        "status": "ready"
    }