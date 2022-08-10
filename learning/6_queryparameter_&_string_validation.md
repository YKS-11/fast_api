# QUERY PARAMETER and STRING VALIDATION

    from fastapi import FastAPI, Query
    from pydantic import Required
    app = FastAPI()
    
    @app.put("/student-detail/{student_id}")
    async def student(student_id: int,  clg: str | None = Query(default=Required, max_length=50)): # validation
        student_data = {"student_id" : student_id, "student_name":"YKS"}
        if clg:
            student_data.update({"college": clg})
        return {"student_id": student_id, **student_data}

##### _min length & max length_
    async def student(student_id: int,  clg: str | None = Query(default=None, max_length=5, max_length=50)): 
    
##### _required_ 
    from pydantic import Required
    async def student(student_id: int,  clg: str | None = Query(default=Required)): 

##### _regular expression_ 
    async def student(student_id: int,  clg: str | None = Query(default=Required, max_length=50, regex="^fixedquery$")): 

##### _default value_
    async def student(student_id: int,  clg: str | None = Query(default="fixedquery", max_length=50)): 

##### _Required with Ellipsis (...)_
    async def student(student_id: int,  clg: str | None = Query(default=..., max_length=50)): 

##### _Query parameter list / multiple values_
    async def student(student_id: int,  clg: list[str] | None = Query(default=Required, min_length=3, max_length=50)): 

##### _Query parameter list / multiple values with defaults_
    async def student(student_id: int,  clg: list[str] | None = Query(default=["vk","yk"])): 

##### _Using list_
    async def student(student_id: int,  clg: list = Query(default=[])):
    
##### _Declare more metadata_ 
    async def student(student_id: int,  clg: str | None = Query(default=None,
        alias="item-query",
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
        max_length=50,
        regex="^fixedquery$",
        deprecated=True,)):

