from sqlalchemy.orm import Session
from . import models, schemas

def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()

def list_students(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Student).offset(skip).limit(limit).all()

def create_student(db: Session, student: schemas.StudentCreate):
    db_obj = models.Student(**student.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_student(db: Session, student_id: int, student: schemas.StudentUpdate):
    db_obj = get_student(db, student_id)
    if not db_obj:
        return None
    for k, v in student.dict(exclude_unset=True).items():
        setattr(db_obj, k, v)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_student(db: Session, student_id: int):
    db_obj = get_student(db, student_id)
    if not db_obj:
        return False
    db.delete(db_obj)
    db.commit()
    return True
