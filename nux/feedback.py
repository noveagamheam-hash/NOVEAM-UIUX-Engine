from typing import Literal
from pydantic import BaseModel, Field

class FeedbackRequest(BaseModel):
    category: Literal["bug", "suggestion", "accessibility", "other"]
    message: str = Field(min_length=5, max_length=2000)
    page: str = Field(default="/", max_length=200)

def validate_feedback(data: FeedbackRequest):
    return {
        "status": "validated",
        "category": data.category,
        "page": data.page,
        "message": data.message,
        "saved": False
    }
