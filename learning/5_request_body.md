# REQUEST BODY 
*for request we using pydantic model

        from fastapi import FastAPI
        from pydantic import BaseModel
        
        class StudentDetail(BaseModel):
            student_name: str
            student_id: str
            student_description: str | None = None

        app = FastAPI()
        
        @app.get("/student-detail/")
        async def student(student_detail: StudentDetail):
            student_detail.student_name.capitalize()
            student_detail.student_id.capitalize()
            return student_detail

