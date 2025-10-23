from sqlalchemy.orm import Session
from . import repository, schemas

class StudentService:
    def __init__(self, db: Session):
        self.db = db

    def get(self, student_id: int):
        return repository.get_student(self.db, student_id)

    def list(self, skip: int = 0, limit: int = 100):
        return repository.list_students(self.db, skip, limit)

    def create(self, student: schemas.StudentCreate):
        return repository.create_student(self.db, student)

    def update(self, student_id: int, student):
        return repository.update_student(self.db, student_id, student)

    def delete(self, student_id: int):
        return repository.delete_student(self.db, student_id)
