# QUERY PARAMETER 

        from fastapi import FastAPI
    
        app = FastAPI()
        
        fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
        
        @app.get("/items/")
        async def read_item(skip: int = 0, limit: int = 10):
            return fake_items_db[skip : skip + limit]
    

### _query passing_ 

        from fastapi import FastAPI
        
        app = FastAPI()
        
        @app.get("/student/{student_id}")
        async def student(student_id: int, student_name: str | None = None):
            if student_name:
                return {"student_id": student_id, "student": student_name}
            return {"student_id": student_id}


### -multi path query parameter_

    http://127.0.0.1:8000/student/1/student_class/A?student_name=YKS&short=false 
        
        from fastapi import FastAPI

        app = FastAPI()
        
        @app.get("/student/{student_id}/student_class/{student_class}")
        async def student(student_id: str, student_class: str, student_name: str | None = None, short: bool = False):
            item = {"student_id": student_id, "student_class": student_class}
            if student_name:
                item.update({"student_name": student_name})
            if not short:
                item.update(
                    {"description": "This is an amazing item that has a long description"}
                )
            return item


### _defining parameter_

        from fastapi import FastAPI
        
        app = FastAPI()
        
        @app.get("/student/{student_id}")
        async def student(student_id: str, student_class: str, student_name: str | None = None, short: bool = False):
            item = {"student_id": student_id, "student_class": student_class}
            if student_name:
                item.update({"student_name": student_name})
            if not short:
                item.update(
                    {"description": "This is an amazing item that has a long description"}
                )
            return item


