# ENUM CLASS
        
        from enum import Enum
        class Color(Enum):
            RED = 1
            GREEN = 2
            BLUE = 3

### _sample prg_

        from enum import Enum
        from fastapi import FastAPI
        
        class StudentName(str, Enum):
            Nisha = "Nisha"
            Prabha = "Prabha"
            santhosh = "santhosh"
        
        app = FastAPI()
        
        @app.get("/student/{student_name}/")
        def student(student_name: StudentName):
            if student_name == StudentName.Nisha:                 # comparing eum memeber
                return {"student_name": student_name, "nick_name": "sapatu sita, driver"}
            if student_name.value == "Prabha":                    # comparing enum value
                return {"student_name": student_name, "nick_name": "DON, Tomato"}
        
            return {"student_name": student_name, "nick_name": "MaRII"}


### _filepath _

* giving the file path 

        from enum import Enum
        from fastapi import FastAPI
        
        app = FastAPI()
        
        @app.get("/student/{file_path:path}")
        def student(file_path : str):
            return {"file_path": file_path}


        






    