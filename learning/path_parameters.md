# path and parameters
    
        get     @app.get()
        post    @app.post()
        put     @app.put()
        delete  @app.delete()
    
        exotic ... options , head, patch, trace



### _only path_


        from fastapi import FastAPI
        
        app = FastAPI()                                     # creating app
        
        @app.get("/")                                       # path operation decorator
        def root():                                         # path operation function
            return {"message": "WELCOME TO FAST API"}


### _path with parameters_ {value}

        from fastapi import FastAPI
    
        app = FastAPI()
        
        @app.get("/student/{id}/")
        async def student(id):
            return {"ROLL_NO": id}

### _path with parameters and datatype_ {value}

        from fastapi import FastAPI
    
        app = FastAPI()
        
        @app.get("/student/{student_name}/")
        def student(student_name: str ):
            return {"ROLL_NO": student_name}

