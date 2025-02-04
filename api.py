from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load marks data from JSON file
with open("q-vercel-python.json", "r") as file:
    students = json.load(file)
    marks_dict = {student["name"]: student["marks"] for student in students}

@app.get("/api")
def get_marks(name: list[str] = Query(...)):
    """API endpoint to fetch marks of given students."""
    return {"marks": [marks_dict.get(n, None) for n in name]}
