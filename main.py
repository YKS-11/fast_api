from enum import Enum
from fastapi import FastAPI

app = FastAPI()

@app.get("/student/{file_path:path}")
def student(file_path : str):
    return {"file_path": file_path}

