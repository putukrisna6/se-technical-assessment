from sqlalchemy import Column, Integer, CheckConstraint
from app.db.base import Base


class Feedback(Base):
    __tablename__ = 'feedbacks'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    score = Column(Integer, CheckConstraint('score >= 1 AND score <= 5'), nullable=False)
