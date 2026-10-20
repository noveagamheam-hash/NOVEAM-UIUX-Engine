from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from nux.themes import get_theme
from nux.accessibility import get_accessibility_defaults
from nux.responsive import get_layout

app = FastAPI(title="NOVEAM UI/UX Engine", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://noveam.in",
        "https://www.noveam.in",
        "http://localhost:5500",
        "http://127.0.0.1:5500"
    ],
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"]
)

@app.get("/")
def home():
    return {"message": "NOVEAM UI/UX Engine Running"}

@app.get("/api/ux/health")
def health():
    return {"service": "NOVEAM UI/UX Engine", "status": "ok"}

@app.get("/api/ux/theme")
def theme(name: str = "light"):
    return get_theme(name)

@app.get("/api/ux/accessibility")
def accessibility():
    return get_accessibility_defaults()

@app.get("/api/ux/layout")
def layout(device: str = "desktop"):
    return get_layout(device)

from nux.personalization import UXPreferences, get_default_preferences, preview_preferences

@app.get("/api/ux/preferences/defaults")
def preferences_defaults():
    return get_default_preferences()

@app.post("/api/ux/preferences/preview")
def preferences_preview(preferences: UXPreferences):
    return preview_preferences(preferences)

from nux.onboarding import OnboardingRequest, get_onboarding_experience

@app.post("/api/ux/onboarding/experience")
def onboarding_experience(data: OnboardingRequest):
    return get_onboarding_experience(data)


from nux.feed import FeedRequest, get_feed_presentation

@app.post("/api/ux/feed/presentation")
def feed_presentation(data: FeedRequest):
    return get_feed_presentation(data)

from nux.navigation import NavigationRequest, get_navigation

@app.post("/api/ux/navigation")
def navigation(data: NavigationRequest):
    return get_navigation(data)

from nux.pwa import PWARequest, get_pwa_experience

@app.post("/api/ux/pwa/experience")
def pwa_experience(data: PWARequest):
    return get_pwa_experience(data)

from nux.feedback import FeedbackRequest, validate_feedback

@app.post("/api/ux/feedback/validate")
def feedback_validate(data: FeedbackRequest):
    return validate_feedback(data)

from nux.analytics import AnalyticsEvent, validate_analytics_event

@app.post("/api/ux/analytics/event")
def analytics_event(data: AnalyticsEvent):
    return validate_analytics_event(data)

from nux.ai_personalization import AIPersonalizationRequest, recommend_experience

@app.post("/api/ux/ai/personalize")
def ai_personalize(data: AIPersonalizationRequest):
    return recommend_experience(data)
