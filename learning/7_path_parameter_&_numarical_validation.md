# Path Parameters and Numeric Validations¶

    The same way you can declare more validations and metadata for query parameters with Query, 
    you can declare the same type of validations and metadata for path parameters with Path.


### _metadata in path_
1st need to import Path from the fastapi

        from fastapi import FastAPI, Query , Path
        app = FastAPI()
        @app.put("/student-detail/{student_id}")
        async def student(student_id: int = Path(title="student id"),  clg: str | None = Query(default=None,
                alias="item-query",
                title="Query string",
                description="Query string for the items to search in the database that have a good match",
                min_length=3,
                max_length=50,
                regex="^fixedquery$",
                deprecated=True,)):
            student_data = {"student_id": student_id, "student_name": "YKS"}
            if clg:
                student_data.update({"college": clg})
            return {"student_id": student_id, **student_data}

### _order parameter_
1. by passing **" * "** to the function.
2. that *, but it will know that all the following parameters should be called as keyword arguments (key-value pairs), also known as kwargs. Even if they don't have a default value.
    
        async def student(*, student_id: int = Path(title="student id"),  clg: str):

### _number validation_
gt: greater than
ge: greater than or equal
lt: less than
le: less than or equal

        async def student(*, student_id: int = Path(title="student id", ge=1, le=10),  clg: str):
