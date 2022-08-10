from fastapi import FastAPI
from pydantic import BaseModel

class StudentDetail(BaseModel):
    student_name: str
    student_roll: str
    student_description: str | None = None
    student_fee: int
    first_graduation_fee: int


app = FastAPI()

@app.put("/student-detail/{student_id}")
async def student(student_id: int, student_detail: StudentDetail, clg: str | None = None):
    student_data = student_detail.dict()
    if clg:
        student_data.update({"college": clg})
    return {"student_id": student_id, **student_data}
