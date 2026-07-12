"""
Term 1 competency seed data (Grade 9 General Mathematics).
Run with: python -m app.core.seed_data

Terms 2 and 3 will be added as new lists in this same file later -
no schema change needed, just more rows.
"""

from app.core.database import SessionLocal, engine, Base
from app.models.competency import Competency
from app.models.user import User  # noqa: F401 - imported so its table is registered before create_all()

TERM_1_COMPETENCIES = [
    {"id": "G9MATH-T1-W01-1", "term": 1, "week_label": "1", "strand": "Measurement and Geometry",
     "order_index": 1, "text": "Illustrate and describe point, line, ray, line segment, angle, and plane using models and geometric notations."},
    {"id": "G9MATH-T1-W01-2", "term": 1, "week_label": "1", "strand": "Measurement and Geometry",
     "order_index": 2, "text": "Construct perpendicular and parallel lines."},

    {"id": "G9MATH-T1-W02-1", "term": 1, "week_label": "2", "strand": "Measurement and Geometry",
     "order_index": 3, "text": "Identify the relationships between angles formed by parallel lines cut by a transversal."},
    {"id": "G9MATH-T1-W02-2", "term": 1, "week_label": "2", "strand": "Measurement and Geometry",
     "order_index": 4, "text": "Determine angle measures involving angle pairs, parallel and perpendicular lines, and parallel lines cut by a transversal."},

    {"id": "G9MATH-T1-W03-1", "term": 1, "week_label": "3-4", "strand": "Number and Algebra",
     "order_index": 5, "text": "Identify relations that are functions based on the definitions of relations and functions."},
    {"id": "G9MATH-T1-W03-2", "term": 1, "week_label": "3-4", "strand": "Number and Algebra",
     "order_index": 6, "text": "Determine the domain and the range of a function expressed in different representations."},
    {"id": "G9MATH-T1-W03-3", "term": 1, "week_label": "3-4", "strand": "Number and Algebra",
     "order_index": 7, "text": "Express the relationship between two variables as a function."},
    {"id": "G9MATH-T1-W03-4", "term": 1, "week_label": "3-4", "strand": "Number and Algebra",
     "order_index": 8, "text": "Determine the slopes (as rate of change) and the zeros of linear functions represented in graphs, equations, and tables of values."},

    {"id": "G9MATH-T1-W05-1", "term": 1, "week_label": "5", "strand": "Number and Algebra",
     "order_index": 9, "text": "Graph a linear function and determine its domain, range, intercepts, and slope."},
    {"id": "G9MATH-T1-W05-2", "term": 1, "week_label": "5", "strand": "Number and Algebra",
     "order_index": 10, "text": "Represent linear relationships found in real-life situations using different representations."},

    {"id": "G9MATH-T1-W06-1", "term": 1, "week_label": "6", "strand": "Number and Algebra",
     "order_index": 11, "text": "Solve problems involving linear functions."},
    {"id": "G9MATH-T1-W06-2", "term": 1, "week_label": "6", "strand": "Measurement and Geometry",
     "order_index": 12, "text": "Determine conditions that guarantee parallelism and perpendicularity of lines."},

    {"id": "G9MATH-T1-W07-1", "term": 1, "week_label": "7-8", "strand": "Measurement and Geometry",
     "order_index": 13, "text": "Classify quadrilaterals based on formal definitions."},
    {"id": "G9MATH-T1-W07-2", "term": 1, "week_label": "7-8", "strand": "Measurement and Geometry",
     "order_index": 14, "text": "Use properties of parallelograms to find measures of angles, sides, perpendicular height, and diagonals."},

    {"id": "G9MATH-T1-W09-1", "term": 1, "week_label": "9", "strand": "Measurement and Geometry",
     "order_index": 15, "text": "Solve problems involving parallelograms, rectangles, squares, or rhombuses by applying their different properties."},

    {"id": "G9MATH-T1-W10-1", "term": 1, "week_label": "10", "strand": "Measurement and Geometry",
     "order_index": 16, "text": "Prove properties of parallelograms by applying the relevant theorems."},
]


def seed():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        existing = db.query(Competency).count()
        if existing > 0:
            print(f"Competencies table already has {existing} rows - skipping seed. "
                  f"Delete existing rows first if you want to reseed.")
            return

        for row in TERM_1_COMPETENCIES:
            db.add(Competency(**row))
        db.commit()
        print(f"Seeded {len(TERM_1_COMPETENCIES)} Term 1 competencies.")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
