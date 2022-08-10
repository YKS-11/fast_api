# REQUEST BODY 
##### for request we using pydantic model

        from fastapi import FastAPI
        from pydantic import BaseModel
        
        class StudentDetail(BaseModel):
            student_name: str
            student_id: str
            student_description: str | None = None

        app = FastAPI()
        
        @app.get("/student-detail/")
        async def student(student_detail: StudentDetail):
            return student_detail

##### post request and operations 

    from fastapi import FastAPI
    from pydantic import BaseModel
    
    class StudentDetail(BaseModel):
        student_name: str
        student_id: str
        student_description: str | None = None
        student_fee: int
        first_graduation_fee: int
    

    app = FastAPI()
    
    @app.post("/student-detail/")
    async def student(student_detail: StudentDetail):
        student_data = student_detail.dict()
        if student_detail.first_graduation_fee:
            fees = student_detail.student_fee - student_detail.first_graduation_fee
            student_data.update({"fees": fees})
        return student_data


##### put request and parameter 

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
    async def student(student_id: int, student_detail: StudentDetail):
        student_data = student_detail.dict()
        if student_detail.first_graduation_fee:
            fees = student_detail.student_fee - student_detail.first_graduation_fee
            student_data.update({"fees": fees})
        return {"student_id": student_id, **student_data}

##### put request + path + query 

    from fastapi import FastAPI
    from pydantic import BaseModel
    
    class StudentDetail(BaseModel):
        student_name: str
        student_roll: str
        student_description: str | None = None
        student_fee: int
        first_graduation_fee: int
    
    
    app = FastAPI()
    
    @app.put("/student-detail/{student_id}")    #path
    async def student(student_id: int, student_detail: StudentDetail, clg: str): #query
        student_data = student_detail.dict()
        if clg:
            student_data.update({"college": clg})
        return {"student_id": student_id, **student_data}