LAYOUTS = {
    "mobile": {"columns": 1, "navigation": "bottom", "sidebar": False},
    "tablet": {"columns": 2, "navigation": "top", "sidebar": False},
    "desktop": {"columns": 3, "navigation": "top", "sidebar": True}
}

def get_layout(device: str = "desktop"):
    selected = device if device in LAYOUTS else "desktop"
    return {"device": selected, "layout": LAYOUTS[selected]}
