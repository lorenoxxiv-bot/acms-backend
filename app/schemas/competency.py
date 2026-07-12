from pydantic import BaseModel


class CompetencyOut(BaseModel):
    id: str
    grade_level: int
    subject: str
    term: int
    week_label: str
    strand: str
    order_index: int
    text: str

    class Config:
        from_attributes = True
