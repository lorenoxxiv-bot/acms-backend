from sqlalchemy import Column, String, Integer
from app.core.database import Base


class Competency(Base):
    """
    One row = one learning competency (one bullet point from the DepEd
    Budget of Work). Deliberately minimal: teacher-facing Content/Performance
    Standards live in curriculum documents, not here. This table only holds
    what the Competency Engine needs to track mastery.
    """
    __tablename__ = "competencies"

    id = Column(String, primary_key=True)  # e.g. "G9MATH-T1-W01-1"
    grade_level = Column(Integer, nullable=False, default=9)
    subject = Column(String, nullable=False, default="General Mathematics")
    term = Column(Integer, nullable=False)  # 1, 2, or 3
    week_label = Column(String, nullable=False)  # "1" or "3-4" (some competencies span weeks)
    strand = Column(String, nullable=False)  # "Measurement and Geometry" | "Number and Algebra" | "Data and Probability"
    order_index = Column(Integer, nullable=False)  # position within the term, for sequencing
    text = Column(String, nullable=False)  # the competency statement itself
