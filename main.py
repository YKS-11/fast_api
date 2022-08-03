from fastapi import FastAPI

app = FastAPI()

@app.get("/student/{student_name}/")
def student(student_name: str ):
    return {"ROLL_NO": student_name}

@app.get("/student")
async def read_users():
    return ["YOGESH", "VIGNESH"]