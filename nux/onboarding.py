from typing import Literal
from pydantic import BaseModel, Field

class OnboardingRequest(BaseModel):
    visit_count: int = Field(default=0, ge=0)
    is_authenticated: bool = False

def get_onboarding_experience(data: OnboardingRequest):
    if not data.is_authenticated:
        return {
            "experience": "visitor",
            "page": "/welcome.html",
            "show_onboarding": True
        }

    if data.visit_count <= 1:
        return {
            "experience": "first_visit",
            "page": "/visitor/onboarding.html",
            "show_onboarding": True
        }

    if data.visit_count == 2:
        return {
            "experience": "second_visit",
            "page": "/home-social.html",
            "show_onboarding": False
        }

    return {
        "experience": "regular_user",
        "page": "/feed.html",
        "show_onboarding": False
    }
