# FAST API 

### _**installation**_ 

        pip install fastapi   

        pip install "uvicorn[standard]"
        

### _**run server**_

    uvicorn main:app --reload


### _**documentation**_
    
    http://127.0.0.1:8000/docs

    http://127.0.0.1:8000/redoc

### **_note_**
    FastAPI is a class that inherits directly from Starlette.
You can use all the [Starlette](https://www.starlette.io/) functionality with FastAPI too.