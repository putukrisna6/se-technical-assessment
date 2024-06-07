from pydantic import BaseModel, Field


class Feedback(BaseModel):
    id: int
    score: int

    class Config:
        orm_mode = True


class FeedbackCreate(BaseModel):
    score: int = Field(..., ge=1, le=5)
