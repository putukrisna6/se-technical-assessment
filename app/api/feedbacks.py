from typing import List, Optional
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.feedback import Feedback, FeedbackCreate
from app.repositories import feedback as feedback_repository
from app.db.session import get_db

router = APIRouter()


@router.get("/feedbacks/", response_model=Optional[List[Feedback]])
async def get_feedbacks(db: Session = Depends(get_db)):
    return await feedback_repository.get_feedbacks(db=db)

@router.post("/feedbacks/", response_model=Feedback)
async def post_feedback(feedback: FeedbackCreate, db: Session = Depends(get_db)):
    return await feedback_repository.post_feedback(db=db, feedback=feedback)