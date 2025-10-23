from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas, service

router = APIRouter(prefix="/students", tags=["students"])

def get_student_service(db: Session = Depends(get_db)):
    return service.StudentService(db)

@router.post("/", response_model=schemas.StudentOut, status_code=201)
def create_student(student: schemas.StudentCreate, svc: service.StudentService = Depends(get_student_service)):
    return svc.create(student)

@router.get("/", response_model=list[schemas.StudentOut])
def list_students(skip: int = 0, limit: int = 100, svc: service.StudentService = Depends(get_student_service)):
    return svc.list(skip, limit)

@router.get("/{student_id}", response_model=schemas.StudentOut)
def get_student(student_id: int, svc: service.StudentService = Depends(get_student_service)):
    obj = svc.get(student_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Student not found")
    return obj

@router.put("/{student_id}", response_model=schemas.StudentOut)
def update_student(student_id: int, student: schemas.StudentUpdate, svc: service.StudentService = Depends(get_student_service)):
    obj = svc.update(student_id, student)
    if obj is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return obj

@router.delete("/{student_id}", status_code=204)
def delete_student(student_id: int, svc: service.StudentService = Depends(get_student_service)):
    ok = svc.delete(student_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Student not found")
    return None
