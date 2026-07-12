from typing import List, Optional
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.competency import Competency
from app.schemas.competency import CompetencyOut

router = APIRouter(prefix="/competencies", tags=["competencies"])


@router.get("", response_model=List[CompetencyOut])
def list_competencies(
    term: Optional[int] = Query(None, description="Filter by term, e.g. 1"),
    db: Session = Depends(get_db),
):
    query = db.query(Competency).order_by(Competency.order_index)
    if term is not None:
        query = query.filter(Competency.term == term)
    return query.all()


@router.get("/{competency_id}", response_model=CompetencyOut)
def get_competency(competency_id: str, db: Session = Depends(get_db)):
    return db.query(Competency).filter(Competency.id == competency_id).first()
