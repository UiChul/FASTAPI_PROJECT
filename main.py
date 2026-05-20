from fastapi import FastAPI
from pydantic import BaseModel
import json
import os

app = FastAPI()

class Course(BaseModel):
    course_name : str
    year : str
    semester : str
    grade : str
    
FILE_PATH = "courses.json"

def read_courses():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)
    
def write_courses(data):
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        
@app.get("/courses")
def get_courses():
    return read_courses() 


@app.post("/courses")
def add_course(course: Course):
    courses = read_courses()        
    courses.append(course.dict())    
    write_courses(courses)         
    
    return {"message": "추가"}