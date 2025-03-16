from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI()

# Enable CORS for the GitHub Pages domain (or any domain you want to allow)
origins = [
    "https://samantha-who.github.io/stunning_tribble",  # Replace this with your exact domain
    "http://localhost",  # Allow requests from localhost for testing
    "http://127.0.0.1",  # Allow requests from localhost (IP address)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow requests from these domains
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# In-memory storage for form data
form_data_storage = []

# Define the form data model
class FormData(BaseModel):
    grammar: str
    opening: int
    callToAction: int
    personalization: int
    persona: int
    business: int
    features: int
    finalScore: float

# POST endpoint to submit form data
@app.post("/submit")
async def submit_form(form_data: FormData):
    form_data_storage.append(form_data.dict())
    return JSONResponse(content={"message": "Form data stored successfully!", "data": form_data.dict()})

# GET endpoint to fetch the submitted grades
@app.get("/grades")
async def get_grades():
    return {"submitted_grades": form_data_storage}
