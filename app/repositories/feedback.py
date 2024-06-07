from sqlalchemy.orm import Session
from sqlalchemy import select
from app.db.models import Feedback as FeedbackSchema
from app.models.feedback import FeedbackCreate


async def get_feedbacks(db: Session):
    result = await db.execute(select(FeedbackSchema).order_by(FeedbackSchema.id))
    return [row for row in result.scalars()]

async def post_feedback(db: Session, feedback: FeedbackCreate):
    new_feedback = FeedbackSchema(score=feedback.score)
    db.add(new_feedback)
    await db.commit()
    await db.refresh(new_feedback)
    return new_feedback